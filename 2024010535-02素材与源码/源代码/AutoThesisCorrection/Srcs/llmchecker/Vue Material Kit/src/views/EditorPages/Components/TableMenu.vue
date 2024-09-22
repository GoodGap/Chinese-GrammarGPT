<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import remixiconUrl from 'remixicon/fonts/remixicon.symbol.svg'
import { Editor } from '@tiptap/vue-3';
const props = defineProps<{
  editor: Editor
}>()
const padding = 10
const tableInfo = reactive({
  rows: 0,
  cols: 0
})
const vueCanvas = ref<CanvasRenderingContext2D>(null)
function drawGrid() {
  vueCanvas.value.fillStyle = "#cfcfcf"
  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      vueCanvas.value.fillRect(padding + 30 * i + 2, padding + 30 * j + 2, 26, 26)
    }
  }
}
/**
 * 实时画图
 * @param event 鼠标移动事件
 */
function onMouseMove(event: MouseEvent) {
  vueCanvas.value.clearRect(0, 0, 260, 260)
  drawGrid()
  const x = event.offsetX - padding
  const y = event.offsetY - padding
  const xi = Math.floor(x / 30)
  const yi = Math.floor(y / 30)
  tableInfo.rows = yi
  tableInfo.cols = xi
  if (xi > 0 && yi > 0) {
    vueCanvas.value.fillStyle = "#000000"
    vueCanvas.value.strokeStyle = "#000000"
    vueCanvas.value.beginPath()
    vueCanvas.value.moveTo(padding, padding)
    vueCanvas.value.lineTo(padding + 30 * xi, padding)
    vueCanvas.value.lineTo(padding + 30 * xi, padding + 30 * yi)
    vueCanvas.value.lineTo(padding, padding + 30 * yi)
    vueCanvas.value.closePath()
    vueCanvas.value.stroke()
  }
}

function insertTable() {
  if (tableInfo.cols > 0 && tableInfo.rows > 0) {
    props.editor.commands.insertTable({ rows: tableInfo.rows, cols: tableInfo.cols, withHeaderRow: false })
    console.log("insert table " + tableInfo.rows + "*" + tableInfo.cols)
  }
}
onMounted(() => {
  console.log(props.editor)
  const canvas = document.getElementById('table-menu-canvas') as HTMLCanvasElement
  const ctx = canvas.getContext('2d')
  vueCanvas.value = ctx
  drawGrid()
})
</script>

<template>
  <div class="dropdown">
    <button class="menu-item dropdown-toggle" title="Table" data-bs-toggle="dropdown" aria-expanded="false">
      <svg class="remix">
        <use :xlink:href="`${remixiconUrl}#ri-table-2`" />
      </svg>
    </button>
    <div class="dropdown-menu">
      <div class="w-100 text-center text-black">
        插入{{ tableInfo.rows }}x{{ tableInfo.cols }}表格
      </div>
      <canvas id="table-menu-canvas" class="border-0 m-0 p-0" width="260" height="260" @mousemove="onMouseMove"
        @click="insertTable">
      </canvas>
    </div>
  </div>
</template>

<style scoped lang="scss">
.menu-item {
  background: transparent;
  border: none;
  border-radius: 0.4rem;
  color: #fff;
  cursor: pointer;
  height: 1.75rem;
  padding: 0.25rem;
  margin-right: 0.25rem;
  width: 1.75rem;

  svg {
    fill: currentColor;
    height: 100%;
    width: 100%;
  }

  &.is-active,
  &:hover {
    background-color: #303030;
  }
}
</style>