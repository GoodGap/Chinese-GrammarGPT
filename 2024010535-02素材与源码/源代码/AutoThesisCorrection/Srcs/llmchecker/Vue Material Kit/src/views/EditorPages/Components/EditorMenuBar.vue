<template>
    <div id="menubar">
        <template v-for="(item, index) in items">
            <div class="divider" v-if="item.type === 'divider'" :key="`divider${index}`" />
            <div class="" v-else-if="item.type === 'tableMenu'" key="tableMenu">
                <table-menu :editor="editor" />
            </div>
            <menu-item v-else :key="index" v-bind="item" />
        </template>
    </div>
</template>
  
<script>
import { Editor } from '@tiptap/vue-3';
import MenuItem from './EditorMenuItem.vue'
import TableMenu from './TableMenu.vue'
export default {
    components: {
        MenuItem,
        TableMenu
    },

    props: {
        editor: {
            type: Editor,
            required: true,
        },
        downloadDocx: {
            type: Function,
            required: true
        },
        save: {
            type: Function,
            required: true
        }
    },

    data() {
        return {
            items: [
                {
                    icon: 'bold',
                    title: 'Bold',
                    action: () => this.editor.chain().focus().toggleBold().run(),
                    isActive: () => this.editor.isActive('bold'),
                },
                {
                    icon: 'italic',
                    title: 'Italic',
                    action: () => this.editor.chain().focus().toggleItalic().run(),
                    isActive: () => this.editor.isActive('italic'),
                },
                {
                    icon: 'strikethrough',
                    title: 'Strike',
                    action: () => this.editor.chain().focus().toggleStrike().run(),
                    isActive: () => this.editor.isActive('strike'),
                },
                {
                    icon: 'code-view',
                    title: 'Code',
                    action: () => this.editor.chain().focus().toggleCode().run(),
                    isActive: () => this.editor.isActive('code'),
                },
                {
                    icon: 'mark-pen-line',
                    title: 'Highlight',
                    action: () => this.editor.chain().focus().toggleHighlight().run(),
                    isActive: () => this.editor.isActive('highlight'),
                },
                {
                    type: 'divider',
                },
                {
                    icon: 'h-1',
                    title: 'Heading 1',
                    action: () => this.editor.chain().focus().toggleHeading({ level: 1 }).run(),
                    isActive: () => this.editor.isActive('heading', { level: 1 }),
                },
                {
                    icon: 'h-2',
                    title: 'Heading 2',
                    action: () => this.editor.chain().focus().toggleHeading({ level: 2 }).run(),
                    isActive: () => this.editor.isActive('heading', { level: 2 }),
                },
                {
                    icon: 'list-unordered',
                    title: 'Bullet List',
                    action: () => this.editor.chain().focus().toggleBulletList().run(),
                    isActive: () => this.editor.isActive('bulletList'),
                },
                {
                    icon: 'list-ordered',
                    title: 'Ordered List',
                    action: () => this.editor.chain().focus().toggleOrderedList().run(),
                    isActive: () => this.editor.isActive('orderedList'),
                },
                {
                    icon: 'list-check-2',
                    title: 'Task List',
                    action: () => this.editor.chain().focus().toggleTaskList().run(),
                    isActive: () => this.editor.isActive('taskList'),
                },
                {
                    icon: 'code-box-line',
                    title: 'Code Block',
                    action: () => this.editor.chain().focus().toggleCodeBlock().run(),
                    isActive: () => this.editor.isActive('codeBlock'),
                },
                {
                    type: 'tableMenu',
                },
                {
                    type: 'divider',
                },
                {
                    icon: 'double-quotes-l',
                    title: 'Blockquote',
                    action: () => this.editor.chain().focus().toggleBlockquote().run(),
                    isActive: () => this.editor.isActive('blockquote'),
                },
                {
                    icon: 'separator',
                    title: 'Horizontal Rule',
                    action: () => this.editor.chain().focus().setHorizontalRule().run(),
                },
                {
                    type: 'divider',
                },
                {
                    icon: 'text-wrap',
                    title: 'Hard Break',
                    action: () => this.editor.chain().focus().setHardBreak().run(),
                },
                {
                    icon: 'format-clear',
                    title: 'Clear Format',
                    action: () => this.editor.chain()
                        .focus()
                        .clearNodes()
                        .unsetAllMarks()
                        .run(),
                },
                {
                    type: 'divider',
                },
                {
                    icon: 'arrow-go-back-line',
                    title: 'Undo',
                    action: () => this.editor.chain().focus().undo().run(),
                },
                {
                    icon: 'arrow-go-forward-line',
                    title: 'Redo',
                    action: () => this.editor.chain().focus().redo().run(),
                },
                {
                    type: 'divider',
                },
                {
                    icon: 'save-2-line',
                    title: 'Save',
                    action: () => this.$props.save(),
                },
                {
                    icon: 'download-2-line',
                    title: 'Download',
                    action: () => this.$props.downloadDocx(),
                }
            ],
        }
    },
}
</script>
  
<style lang="scss" scoped>
.divider {
    background-color: rgba(#fff, 0.25);
    height: 1.25rem;
    margin-left: 0.5rem;
    margin-right: 0.75rem;
    width: 1px;
}

#menubar {
    align-items: center;
    background: #0d0d0d;
    border-bottom: 3px solid #0d0d0d;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem;
    display: flex;
    flex: 0 0 auto;
    flex-wrap: wrap;
    padding: 0.25rem;
}
</style>