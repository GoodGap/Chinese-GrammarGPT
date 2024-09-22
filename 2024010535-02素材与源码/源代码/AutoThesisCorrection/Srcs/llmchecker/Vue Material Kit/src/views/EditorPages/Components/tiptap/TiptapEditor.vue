
<script setup lang="ts">
import { computed, ref, watchEffect, onMounted, onUnmounted, reactive } from 'vue'
import { useEditor, EditorContent, Editor } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import Highlight from '@tiptap/extension-highlight'
import CodeBlock from '@tiptap/extension-code-block'
import TaskItem from '@tiptap/extension-task-item'
import TaskList from '@tiptap/extension-task-list'
import { LanguageTool, LanguageToolHelpingWords, BubbleMenu, IssueType } from './extensions'
import { content } from './text'
import { Match } from '@/types'
import { TextSelection } from 'prosemirror-state'
import EditorMenuBar from '@/views/EditorPages/Components/EditorMenuBar.vue'
import Table from '@tiptap/extension-table'
import TableCell from '@tiptap/extension-table-cell'
import TableHeader from '@tiptap/extension-table-header'
import TableRow from '@tiptap/extension-table-row'
import { convertDocxToHTML } from '@/tools/doc-tool'
import { requestFile, updateFile, uploadFile } from '@/server/file'
import { useUserStore } from '@/stores/user'
import Image from '@tiptap/extension-image'
import axios from 'axios'
const props = withDefaults(defineProps<{
  filename: string
}>(), { filename: "test.docx" })

const userStore = useUserStore();
const loadFileState = reactive({
  loading: true,
  error: false,
  success: false,
  timeout: false,
})
onMounted(async () => {
  loadFileState.loading = true;
  requestFile(userStore.userDetail.username, props.filename).then(async (res) => {
    console.log('编辑器接收内容', res);
    convertDocxToHTML(res.data).then((res) => {
      console.log('编辑器准备渲染', res);
      editor.value.commands.setContent(res);
      loadFileState.loading = false;
      loadFileState.success = true
    }).catch((err) => {
      console.log("解析文件失败", err);
      loadFileState.loading = false;
      loadFileState.error = true;
    });
  }).catch((err) => {
    if (err.response.status == 408) {
      loadFileState.loading = false;
      loadFileState.timeout = true;
    } else {
      console.log('加载文件失败', err);
      loadFileState.loading = false;
      loadFileState.error = true;
    }
  });
})
interface Error {
  from_: number,
  to_: number,
  message: string,
  errorWord: string,
  replacements: any,
  match__: Match
}



const shouldShow = ({ editor }) => {
  const match = editor.storage.languagetool.match
  const matchRange = editor.storage.languagetool.matchRange
  const { from, to } = editor.state.selection
  // 修改
  // const languageToolPlugin = editor.view.state.plugins.find((plugin) => plugin.key.startsWith('languagetool'))
  //
  // let decorationSet // 在 if 语句之前声明 decorationSet
  // if (languageToolPlugin) {
  //   decorationSet = languageToolPlugin.props.decorations(editor.state)
  // }
  // console.log(decorationSet)
  // 修改 OVER

  // console.log(editor);
  console.log('PPPP')
  // console.log(from);
  // console.log(to);
  console.log(match)
  console.log(matchRange)
  // console.log(!!match && !!matchRange && matchRange.from <= from && to <= matchRange.to);
  console.log('TTTTT')
  console.log(showcard.value)
  console.log((!!match && !!matchRange && matchRange.from <= from && to <= matchRange.to) || showcard.value)
  return (!!match && !!matchRange && matchRange.from <= from && to <= matchRange.to) || showcard.value
}

const match = ref<Match>(null)

const matchRange = ref<{ from: number; to: number }>(null)

const loading = ref(false)

const showcard = ref(false)

const showHeadingDropdown = ref(false)

const applyHeading = (level: number, editorInstance) => {
  console.log(editor)
  editorInstance.chain().focus().setHeading({ level }).run()
  showHeadingDropdown.value = false
}

const updateMatch = (editor: Editor) => {
  match.value = editor.storage.languagetool.match
  matchRange.value = editor.storage.languagetool.matchRange
}

const editor = useEditor({
  extensions: [
    StarterKit,
    Highlight,
    CodeBlock,
    TaskList,
    TaskItem.configure({
      nested: true
    }),
    LanguageTool.configure({
      automaticMode: true,
      documentId: '1',
      apiUrl: 'http://222.20.97.104:8081/correct/',
    }),
    Table as any,
    TableCell,
    TableHeader,
    TableRow,
    Image.configure({
      inline: true,
      allowBase64: true,
    })
  ],
  onUpdate({ editor }) {
    setTimeout(() => updateMatch(editor as any))
  },
  onSelectionUpdate({ editor }) {
    setTimeout(() => updateMatch(editor as any))
  },
  onTransaction({ transaction: tr }) {
    if (tr.getMeta(LanguageToolHelpingWords.LoadingTransactionName)) loading.value = true
    else loading.value = false
  },
})

const decorationSet = ref(null)

function extractErrors(obj, errors: Array<Error> = []) {

  console.log('WWWWWW')
  console.log(obj.children)
  let index = 2
  let result = []
  for (let k = 0; k < obj.local.length; k++) {
    let match_local = obj.local[k].type.attrs.match
    match_local = JSON.parse(match_local)
    const message_local = match_local.match.message
    const replacements_local = match_local.match.replacements[0].value
    const from_local = match_local.from
    const to_local = match_local.to

    let errorWord_local = ''
    console.log(message_local)
    if (message_local.match(/'([^']+)'/)) {
      errorWord_local = message_local.match(/'([^']+)'/)[1]
    }
    console.log('push error')
    errors.push({
      from_: from_local,
      to_: to_local,
      message: message_local,
      errorWord: errorWord_local,
      replacements: replacements_local,
      match__: match_local.match as Match,
    })

  }
  console.log('errors 222')
  console.log(errors)
  while (index < obj.children.length) {
    result.push(obj.children[index])
    index += 3
  }

  console.log(result)
  for (let i = 0; i < result.length; i++) {
    for (let j = 0; j < result[i].local.length; j++) {
      // console.log(result[i].local[j])
      let match_ = result[i].local[j].type.attrs.match
      match_ = JSON.parse(match_)
      const match__ = match_.match
      // console.log(typeof match_);
      console.log(match_)
      const message = match_.match.message
      const replacements = match_.match.replacements[0].value
      const from_ = match_.from
      const to_ = match_.to
      let errorWord = ''
      if (message.match(/'([^']+)'/)) {
        errorWord = message.match(/'([^']+)'/)[1]
      }

      // console.log(message);
      // console.log(replacements);
      // console.log(typeof from_);
      // console.log(typeof to_);
      errors.push({ from_, to_, message, errorWord, replacements, match__ })
    }
  }
  errors.sort((a, b) => a.from_ - b.from_)
  return errors
  // if (obj.local) {
  //   obj.local.forEach((error) => {
  //     const match = JSON.parse(error.type.attrs.match)
  //     const message = match.message
  //     const replacements = match.replacements.map((replacement) => replacement.value)
  //     errors.push({ message, replacements })
  //   })
  // }
  //
  // if (obj.children) {
  //   obj.children.forEach((child) => {
  //     if (typeof child === 'object') {
  //       extractErrors(child, errors)
  //     }
  //   })
  // }
  //
  // return errors
}

const errors = computed(() => {
  if (decorationSet.value) {
    return extractErrors(decorationSet.value)
  }

  return []
})
watchEffect(() => {
  if (!editor.value) {
    return
  }

  const languageToolPlugin = editor.value.view.state.plugins.find((plugin: any) =>
    plugin.key.startsWith('languagetool'),
  )

  // if (languageToolPlugin) {
  //   decorationSet.value = languageToolPlugin.props.decorations(editor.value.state);
  // }
  if (languageToolPlugin) {
    const plugin: any = languageToolPlugin
    decorationSet.value = plugin.props.decorations(editor.value.state)
  }
})

const replacements = computed(() => match.value?.replacements || [])

const matchMessage = computed(() => match.value?.message || 'No Message')

const highlightedMatchMessage = computed(() => {
  if (!matchMessage.value.match(/'([^']+)'/)) {
    return matchMessage.value
  }

  const errorWord = matchMessage.value.match(/'([^']+)'/)[1]
  const highlightedWord = `<span class="highlighted-word">${errorWord}</span>`
  return matchMessage.value.replace(`'${errorWord}'`, highlightedWord)
})

const updateHtml = () => navigator.clipboard.writeText(editor.value.getHTML())

const acceptSuggestion = (sug) => {
  // console.log("CCCC");
  // console.log(editor.value.storage.languagetool.matchRange);
  console.log('CCCC')
  console.log(sug.value)
  console.log(editor.value.storage.languagetool.matchRange)

  if (sug.value == "") { // delete
    editor.value.commands.deleteRange(matchRange.value)
  } else { // replace and insert
    editor.value.commands.insertContentAt(matchRange.value, sug.value)
  }
  editor.value.storage.languagetool.matchRange = {}
  showcard.value = false
}

const acceptSuggestion_card = (error) => {
  setSelectionToDecoration(error.from_, error.to_)
  editor.value.storage.languagetool.match = error.match__
  editor.value.storage.languagetool.matchRange = { from: error.from_, to: error.to_ }

  // console.log('CCCC')
  // console.log(error.replacements)
  // console.log(editor.value.storage.languagetool.matchRange)

  if (error.replacements == "") {
    editor.value.commands.deleteRange(editor.value.storage.languagetool.matchRange)
  } else {
    editor.value.commands.insertContentAt(editor.value.storage.languagetool.matchRange, error.replacements)
  }
  editor.value.storage.languagetool.matchRange = {}

  // console.log('VVVVVVV')
  // console.log(showcard.value)
}

const handleCardClick = (error, index) => {
  console.log('FFFFFF')
  console.log(error)
  console.log(index)
  // 调用 setSelectionToDecoration 函数来设置选区
  setSelectionToDecoration(error.from_, error.to_)
  editor.value.storage.languagetool.match = error.match__
  editor.value.storage.languagetool.matchRange = { from: error.from_, to: error.to_ }
  console.log(editor.value.storage.languagetool.match)
  showcard.value = true
}

// 监听文档的点击事件
onMounted(() => {
  document.addEventListener('click', onDocumentClick)
})

// 移除文档的点击事件监听
onUnmounted(() => {
  document.removeEventListener('click', onDocumentClick)
})

function setSelectionToDecoration(from, to) {
  // 创建一个新的事务
  const tr = editor.value.state.tr

  // 设置选区
  const newSelection = TextSelection.create(editor.value.state.doc, from, to)
  tr.setSelection(newSelection)

  // 更新编辑器状态
  editor.value.view.dispatch(tr)
}

const onDocumentClick = (event) => {
  if (!event.target.closest('.error-card') && !event.target.closest('bubble-menu')) {
    showcard.value = false
  }
}

const proofread = () => editor.value.commands.proofread()

const ignoreSuggestion = () => {
  editor.value.commands.ignoreLanguageToolSuggestion()
}
const ignore_once = () => {
  editor.value.commands.ignoreSuggestionOnce()
}

const ignoreSuggestion_card = (error) => {
  setSelectionToDecoration(error.from_, error.to_)
  editor.value.storage.languagetool.match = error.match__
  editor.value.storage.languagetool.matchRange = { from: error.from_, to: error.to_ }
  editor.value.commands.ignoreLanguageToolSuggestion()
}

const ignore_once_card = (error) => {
  setSelectionToDecoration(error.from_, error.to_)
  editor.value.storage.languagetool.match = error.match__
  editor.value.storage.languagetool.matchRange = { from: error.from_, to: error.to_ }
  editor.value.commands.ignoreSuggestionOnce()
}

function onErrorCardEnter(error: Error) {
  editor.value.commands.focus(error.to_)
}
/**
 * 在表格中插入行或列
 * @param position 插入位置
 */
function insertTableLine(position: "above" | "below" | "left" | "right") {
  switch (position) {
    case "above":
      editor.value.commands.addRowBefore()
      break;
    case "below":
      editor.value.commands.addRowAfter()
      break;
    case "left":
      editor.value.commands.addColumnBefore()
      break;
    case "right":
      editor.value.commands.addColumnAfter()
      break;
    default:
      break;
  }
}

function deleteTableElement(lineType: "row" | "column" | "table") {
  switch (lineType) {
    case "row":
      editor.value.commands.deleteRow()
      break;
    case "column":
      editor.value.commands.deleteColumn()
      break;
    case "table":
      editor.value.commands.deleteTable()
      break;
    default:
      break;
  }
}

/**
 * 保存为 docx 文件
 */
async function downloadDocx() {
  await saveDocx();
  console.log("提取文本", editor.value.getText())
  console.log("提取JSON", editor.value.getJSON())
  const blob = (await requestFile(userStore.userDetail.username, props.filename)).data
  const url = URL.createObjectURL(blob)
  const a = document.createElement("a")
  a.href = url
  a.download = props.filename
  a.click()
  URL.revokeObjectURL(url)
}

/**
 * 保存并上传
 */
async function saveDocx() {
  await updateFile(
    editor.value.getHTML(),
    userStore.userDetail.username,
    props.filename,
    userStore.userDetail.token,
  )
}
</script>

<template>
  <!--  <section class="editor-menubar">-->
  <!--    <button @click="updateHtml">Copy editor html</button>-->
  <!--    <button @click="proofread">Proofread</button>-->
  <!--    <span>{{ loading ? 'Loading' : 'Done' }}</span>-->
  <!--  </section>-->
  <div class="main-container">
    <div class="editor-container">
      <EditorMenuBar v-if="editor" :editor="editor" :downloadDocx="() => downloadDocx()" :save="() => saveDocx()" />
      <editor-content class="tiptap-editor" v-if="loadFileState.success" :editor="editor" />
      <!-- loding -->
      <div v-else-if="loadFileState.loading">
        <div class="spinner-border"></div>
        <p>正在加载文件，请稍候...</p>
      </div>
      <!-- error -->
      <div v-else-if="loadFileState.error" class="loading">
        <p>加载文件失败</p>
      </div>
      <!-- timeout -->
      <div v-else-if="loadFileState.timeout" class="loading">
        <p>加载文件超时，请检查网络连接或者联系管理员</p>
      </div>

    </div>
    <div class="info-list">
      <div class="error-list">
        <template v-if="errors.length > 0">
          <div v-for="(error, index) in errors" :key="index" class="error-card" @click="handleCardClick(error, index)"
            @mouseenter="onErrorCardEnter(error)">
            <div class="error-word">
              <div v-if="(error.match__ as Match).rule.issueType == IssueType.Replace">
                <span>{{ error.errorWord }}</span>
                <span class="arrow">&#8594;</span>
                <span>{{ error.replacements }}</span>
              </div>
              <div v-else-if="(error.match__ as Match).rule.issueType == IssueType.Insert">
                <span>{{ error.errorWord }}</span>
                <span class="arrow">+</span>
                <span>{{ error.replacements }}</span>
              </div>
              <div v-else-if="(error.match__ as Match).rule.issueType == IssueType.Delete">
                <span class="arrow">-</span>
                <span>{{ error.errorWord }}</span>
              </div>
              <div v-else>
                <span>{{ error.errorWord }}</span>
              </div>

            </div>
            <div class="message">{{ error.message }}</div>

            <div class="buttons">
              <button class="btn" v-if="error.match__ && (error.match__ as Match).rule.issueType == IssueType.Replace"
                @click="($event) => {
                  $event.stopPropagation()
                  acceptSuggestion_card(error)
                }
                  ">修改为：{{ error.replacements }}</button>
              <button class="btn" v-else-if="(error.match__ as Match).rule.issueType == IssueType.Insert" @click="($event) => {
                $event.stopPropagation()
                acceptSuggestion_card(error)
              }
                ">插入: {{ error.replacements }}</button>
              <button class="btn" v-else-if="(error.match__ as Match).rule.issueType == IssueType.Delete" @click="($event) => {
                $event.stopPropagation()
                acceptSuggestion_card(error)
              }
                ">删除内容</button>
              <button class="btn" @click="($event) => {
                $event.stopPropagation()
                acceptSuggestion_card(error)
              }" v-else>纠正为：{{ error.replacements }}</button>

              <button class="ignore-once-button" @click="($event) => {
                $event.stopPropagation()
                ignore_once_card(error)
              }
                ">忽略一次
              </button>
              <button class="ignore-suggestion-button" @click="($event) => {
                $event.stopPropagation()
                ignoreSuggestion_card(error)
              }
                ">
                永久忽略
              </button>
            </div>
          </div>
        </template>
        <template v-else>
          <div class="loading">
            <div class="spinner"></div>
            <p>正在检查错误，请稍候...</p>
          </div>
        </template>
      </div>
    </div>
  </div>
  <!-- 表格编辑菜单 -->
  <BubbleMenu plugin-key="menu-table-cell" v-if="editor" :editor="editor"
    :should-show="({ editor }) => editor.isActive('table')" :tippy-options="{ placement: 'right' }">
    <div class="dropdown dropdown-hover p-0 mt-0 z-index-3">
      <div id="dropdownTableMenu" class="align-items-center cursor-pointer ps-4" data-bs-toggle="dropdown"
        aria-expanded="false">
        <i class="bi bi-pencil-square bg-white" />
      </div>
      <div class="dropdown-menu dropdown-menu-dark border-1 p-2" aria-labelledby="dropdownTableMenu">
        <div class="dropdown dropdown-hover dropdown-subitem border-1 p-0">
          <div class="dropdown-item d-flex justify-content-between">
            <div>插入</div>
            <i class="bi bi-caret-right-fill"></i>
          </div>
          <ul class="dropdown-menu dropdown-menu-dark p-2">
            <li class="dropdown-item" @click="insertTableLine('above')">
              在上方插入行
            </li>
            <li class="dropdown-item" @click="insertTableLine('below')">
              在下方插入行
            </li>
            <li class="dropdown-item" @click="insertTableLine('left')">
              在左侧插入列
            </li>
            <li class="dropdown-item" @click="insertTableLine('right')">
              在右侧插入列
            </li>
          </ul>
        </div>
        <div class="dropdown dropdown-hover dropdown-subitem border-1 p-0">
          <div class="dropdown-item d-flex justify-content-between">
            <div>删除</div>
            <i class="bi bi-caret-right-fill"></i>
          </div>
          <ul class="dropdown-menu dropdown-menu-dark p-2">
            <li class="dropdown-item" @click="deleteTableElement('row')">
              删除整行
            </li>
            <li class="dropdown-item" @click="deleteTableElement('column')">
              删除整列
            </li>
            <li class="dropdown-item" @click="deleteTableElement('table')">
              删除表
            </li>
          </ul>
        </div>
        <div class="dropdown-item" @click="editor.commands.mergeCells()">
          合并单元格
        </div>
        <div class="dropdown-item" @click="editor.commands.splitCell()">
          拆分单元格
        </div>
      </div>
    </div>

  </BubbleMenu>
  <bubble-menu class="bubble-menu" v-if="editor" :editor="editor"
    :tippy-options="{ placement: 'bottom', animation: 'fade' }" :should-show="({ editor }) => shouldShow({ editor })">
    <section class="bubble-menu-section-container">
      <section class="bubble-menu-section-container">
        <section class="message-section" v-html="highlightedMatchMessage"></section>
      </section>
      <section class="suggestions-section">
        <article v-for="(replacement, i) in replacements" @click="() => acceptSuggestion(replacement)"
          :key="i + replacement.value" class="suggestion">
          <div v-if="match.rule.issueType == IssueType.Replace">
            修改为：{{ replacement.value }}
          </div>
          <div v-else-if="match.rule.issueType == IssueType.Insert">
            插入：{{ replacement.value }}
          </div>
          <div v-else-if="match.rule.issueType == IssueType.Delete">
            删除内容
          </div>
          <div v-else>
            纠正为：{{ replacement.value }}
          </div>
        </article>
      </section>
      <section class="action-section">
        <button class="ignore-once-button" @click="ignore_once">仅忽略一次</button>
        <button class="ignore-suggestion-button" @click="ignoreSuggestion">永久忽略</button>
      </section>
    </section>
  </bubble-menu>
</template>


<style lang="scss">
//.editor-menubar {
//  display: flex;
//  gap: 1rem;
//
//  button {
//    padding: 0.5rem;
//    text-transform: capitalize;
//    border: none;
//    background-color: white;
//    box-shadow: 0 0 10px rgba($color: #000000, $alpha: 0.25);
//    border-radius: 6px;
//    cursor: pointer;
//    transition: all 0.2s ease-in-out;
//    font-weight: 500;
//    font-size: 1.1em;
//
//    &:hover {
//      box-shadow: 0 0 2px rgba($color: #000000, $alpha: 0.25);
//    }
//  }
//}

.main-container {
  display: flex;
  width: 80%;
  height: 100%;
  margin: 0 auto;
}

.editor-container {
  display: flex;
  flex-direction: column;
  width: 80%;
  height: 86vh;
}

.info-list {
  height: 86vh;
  width: 30%;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f5f5f5;
  margin-left: 1rem;
  position: relative; // 添加此属性
  max-height: calc(100vh - 2rem); // 根据页面布局设置此值
  overflow: hidden; // 添加此属性
}

.error-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: absolute; // 添加此属性
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  overflow-y: auto; // 添加此属性
  padding-right: 8px; // 添加此属性，以避免滚动条遮挡内容
}

.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 2rem;
  text-align: center;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #007bff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  100% {
    transform: rotate(360deg);
  }
}

.error-card {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);

  .error-word {
    display: flex;
    align-items: center;
    gap: 8px;

    .arrow {
      font-size: 24px;
    }
  }

  .message {
    margin-top: 8px;
    font-size: 14px;
    color: #6c757d;
    text-align: left;
  }

  .buttons {
    display: flex;
    justify-content: space-between;
    margin-top: 16px;

    .btn {
      background-color: #007bff;
      color: #fff;
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 14px;
      border: none;
      cursor: pointer;
      transition: background-color 0.2s;

      &:hover {
        background-color: #0056b3;
      }
    }

    .ignore-once-button {
      background-color: #4b4b4b;
      color: white;
      border-radius: 8px;
      padding: 8px;
      font-size: 1.1em;
      font-weight: 500;
      cursor: pointer;
      border: none;
      transition: background-color 0.3s ease;

      &:hover {
        background-color: #6d6d6d;
      }
    }

    .ignore-suggestion-button {
      background-color: #ff453a;
      color: white;
      border-radius: 8px;
      padding: 8px;
      font-size: 1.1em;
      font-weight: 500;
      cursor: pointer;
      border: none;
      transition: background-color 0.3s ease;

      &:hover {
        background-color: #ff6c5e;
      }
    }
  }
}

//.info-list {
//  flex: 1;
//  max-width: 33.33%;
//  min-width: 33.33%;
//  padding: 1rem;
//  border: 1px solid #ccc;
//  border-radius: 4px;
//  background-color: #f5f5f5;
//  margin-left: 1rem;
//  overflow-y: auto;
//
//  .info-item {
//    padding: 0.5rem 1rem;
//    background-color: #fff;
//    border: 1px solid #ccc;
//    border-radius: 4px;
//    margin-bottom: 0.5rem;
//    font-size: 0.9em;
//    transition: all 0.2s ease-in-out;
//
//    &:hover {
//      background-color: #f0f0f0;
//      border-color: #999;
//    }
//  }
//}

.editor-menubar {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background-color: #f5f5f5;
  border-bottom: 1px solid #e0e0e0;

  .button-common {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.5rem 0.75rem;
    text-transform: uppercase;
    border: none;
    background-color: #3f51b5;
    color: white;
    box-shadow: 0 0 10px rgba($color: #000000, $alpha: 0.25);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease-in-out;
    font-weight: 500;
    font-size: 0.9em;
    line-height: 1.5; // 添加这一行来设置固定的行高

    &:hover {
      box-shadow: 0 0 2px rgba($color: #000000, $alpha: 0.25);
      background-color: #283593;
    }
  }

  button {
    @extend .button-common;

    // 设置图标大小
    i {
      font-size: 1em;
      margin-right: 0.3em;
      margin-left: 0.3em;
    }

    // 设置包含图标和文字的按钮的宽度
    &:not(:only-child) {
      min-width: 60px;
    }
  }

  // 下拉菜单样式
  .dropdown {
    position: relative;
    display: inline-block;
  }

  .dropdown-menu {
    display: none;
    position: absolute;
    min-width: 120px; // 修改此处以调整下拉菜单宽度
    padding: 5px 0;
    margin: 2px 0 0;
    background-color: #f5f5f5;
    border: 1px solid #e0e0e0;
    box-shadow: 0 0 10px rgba($color: #000000, $alpha: 0.25);
    border-radius: 6px;
    z-index: 1;

    button {
      @extend .button-common;
      display: block;
      width: 100%;
      padding: 5px 20px;
      clear: both;
      font-weight: 500;
      text-align: left;
      white-space: nowrap;
      background-color: #343541; // 修改此处以调整下拉菜单按钮背景颜色
      border: 0;

      &:hover {
        background-color: #3f51b5;
        color: white;
      }
    }
  }

  .dropdown:hover .dropdown-menu {
    display: block;
  }

  .status {
    margin-left: auto;
    display: flex;
    align-items: center;

    .loading-container {
      width: 20px;
      height: 20px;
      margin-right: 0.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .loading-spinner {
      border: 2px solid #3f51b5;
      border-top: 2px solid transparent;
      border-radius: 50%;
      width: 20px;
      height: 20px;
      animation: spin 1s linear infinite;
      opacity: 0;
      transition: opacity 0.3s ease;
    }

    .visible {
      opacity: 1;
    }

    span {
      font-size: 0.9em;
      font-weight: 500;
      color: #3f51b5;
      margin-left: 0.5rem;
      padding: 2px 6px;
      border-radius: 3px;
      background-color: rgba(63, 81, 181, 0.1);
    }

    @keyframes spin {
      100% {
        transform: rotate(360deg);
      }
    }
  }
}

.ProseMirror {
  color: black;

  p {
    font-weight: normal;
  }

  &:focus {
    outline: none;
  }

  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 100%;
    margin: 0;
    overflow: hidden;

    td,
    th {
      min-width: 1em;
      border: 2px solid #ced4da;
      padding: 3px 5px;
      vertical-align: top;
      box-sizing: border-box;
      position: relative;

      >* {
        margin-bottom: 0;
      }
    }

    th {
      font-weight: bold;
      text-align: left;
      background-color: #f1f3f5;
    }

    .selectedCell:after {
      z-index: 2;
      position: absolute;
      content: "";
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      background: rgba(200, 200, 255, 0.4);
      pointer-events: none;
    }

    .column-resize-handle {
      position: absolute;
      right: -2px;
      top: 0;
      bottom: -2px;
      width: 4px;
      background-color: #adf;
      pointer-events: none;
    }

    p {
      margin: 0;
    }
  }

  blockquote {
    padding-left: 1rem;
    border-left: 3px solid rgba(#0D0D0D, 0.1);
  }

  ul[data-type="taskList"] {
    list-style: none;
    padding: 0;

    p {
      margin: 0;
    }

    li {
      display: flex;

      >label {
        flex: 0 0 auto;
        margin-right: 0.5rem;
        user-select: none;
      }

      >div {
        flex: 1 1 auto;
      }
    }
  }

  hr {
    border-top: 1px solid;
  }

  hr.ProseMirror-selectednode {
    border-top: 1px solid #68CEF8;
  }

  code {
    font-size: 0.9rem;
    padding: 0.25em;
    border-radius: 0.25em;
    background-color: rgba(#616161, 0.1);
    color: #616161;
    box-decoration-break: clone;
  }

  pre {
    background: #0D0D0D;
    color: #FFF;
    font-family: 'JetBrainsMono', monospace;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;

    code {
      color: inherit;
      padding: 0;
      background: none;
      font-size: 0.8rem;
    }
  }



  .lt {
    //border-bottom: 2px solid #e86a69;
    transition: background 0.25s ease-in-out;

    // &:hover {
    //   background: rgba($color: #e86a69, $alpha: 0.2);
    // }

    &-style {
      border-bottom: 2px solid #9d8eff;

      &:hover {
        background: rgba($color: #9d8eff, $alpha: 0.2) !important;
      }
    }

    &-typographical,
    &-grammar {
      border-bottom: 2px dotted #eeb55c;

      &:hover {
        background: rgba($color: #eeb55c, $alpha: 0.2) !important;
      }
    }

    // 拼写错误
    &-misspelling {
      border-bottom: 2px solid #e86a69;

      &:hover {
        background: rgba($color: #e86a69, $alpha: 0.2) !important;
      }
    }

    // 替换型错误 12[34]56 -> 12[789]56
    &-replace {
      border-bottom: 2px solid #e86a69;

      &:hover {
        background: rgba($color: #e86a69, $alpha: 0.2) !important;
      }
    }

    // 删除型错误 12[34]56 -> 12[]56
    &-delete {
      // border-bottom: 2px dotted #eeb55c;
      text-decoration: line-through 1px rgba($color: #e86a69, $alpha: 0.5);


      &:hover {
        background: rgba($color: #e86a69, $alpha: 0.2) !important;
      }
    }

    // 插入型错误 12[]56 -> 12[34]56
    &-insert {
      border-bottom: 2px dotted #eeb55c;

      &:hover {
        background: rgba($color: #eeb55c, $alpha: 0.2) !important;
      }
    }
  }

  &-focused {
    outline: none !important;
  }
}

.flex {
  display: flex;

  div {
    width: 50%;
  }
}

//.content {
//  max-width: 50%;
//  min-width: 50%;
//}

.tiptap-editor {
  flex: 12;
  padding: 4px;
  border: 1px solid #ccc;
  border-radius: 0 0 4px 4px;
  font-family: 'Arial', sans-serif;
  font-size: 14px;
  line-height: 1.5;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  text-align: left;
  overflow: scroll;

  &:focus {
    border-color: #66afe9;
    outline: 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.12), 0 4px 6px rgba(0, 0, 0, 0.24);
  }
}

//.bubble-menu > .bubble-menu-section-container {
//  display: flex;
//  flex-direction: column;
//  background-color: white;
//  padding: 8px;
//  border-radius: 8px;
//  box-shadow: 0 0 10px rgba($color: black, $alpha: 0.25);
//  max-width: 400px;
//
//  .suggestions-section {
//    display: flex;
//    flex-direction: row;
//    flex-wrap: wrap;
//    gap: 4px;
//    margin-top: 1em;
//
//    .suggestion {
//      background-color: #229afe;
//      border-radius: 4px;
//      color: white;
//      cursor: pointer;
//      font-weight: 500;
//      padding: 4px;
//      display: flex;
//      align-items: center;
//      font-size: 1.1em;
//      max-width: fit-content;
//    }
//  }
//}

.bubble-menu>.bubble-menu-section-container {
  display: flex;
  flex-direction: column;
  background-color: #1c1c1e;
  padding: 12px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba($color: black, $alpha: 0.5);
  max-width: 400px;

  .message-section {
    color: white;
    font-size: 1.2em;
    font-weight: 500;
    margin-bottom: 8px;
    //text-align: left;

    .highlighted-word {
      color: #ff9f00;
      font-weight: 600;
    }
  }

  .suggestions-section {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-bottom: 8px;

    .suggestion {
      background-color: #3a3b3c;
      border-radius: 8px;
      color: white;
      cursor: pointer;
      font-weight: 500;
      padding: 8px;
      font-size: 1.1em;
      transition: background-color 0.3s ease;
      width: 100%;
      text-align: left;
      box-sizing: border-box;

      &:hover {
        background-color: #007aff;
      }
    }
  }

  .action-section {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;

    .ignore-once-button {
      background-color: #4b4b4b;
      color: white;
      border-radius: 8px;
      padding: 8px;
      font-size: 1.1em;
      font-weight: 500;
      cursor: pointer;
      border: none;
      transition: background-color 0.3s ease;

      &:hover {
        background-color: #6d6d6d;
      }
    }

    .ignore-suggestion-button {
      background-color: #ff453a;
      color: white;
      border-radius: 8px;
      padding: 8px;
      font-size: 1.1em;
      font-weight: 500;
      cursor: pointer;
      border: none;
      transition: background-color 0.3s ease;

      &:hover {
        background-color: #ff6c5e;
      }
    }
  }
}
</style>
