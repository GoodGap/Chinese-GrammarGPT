<script setup lang="ts">
import NavbarDefault from '@/examples/navbars/NavbarDefault.vue';
import { TiptapEditor } from '@/views/EditorPages/Components/tiptap';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
const route = useRouter().currentRoute;
console.log("当前路由", route);

</script>


<template>
  <NavbarDefault dark transparent class="mt-0" />
  <div id="editor" class="row pt-3">
    <div class="col">
      <TiptapEditor :filename="(route.params.filename as string)" />
    </div>
  </div>
</template>

<style scoped>
html,
body {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}

#app {
  height: 100%;
  width: 100%;
  padding: 0;
}

#editor {
  position: absolute;
  top: 10vh;
  width: 100%;
  height: 90vh;
  padding: 0;
}
</style>