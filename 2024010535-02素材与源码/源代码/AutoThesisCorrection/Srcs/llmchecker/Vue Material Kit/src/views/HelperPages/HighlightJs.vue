<template>
    <hljsVuePlugin.component :code="code" autodetect class="hljs" />
</template>

<script setup lang="ts">

import hljsVuePlugin from "@highlightjs/vue-plugin";

const props = defineProps<{
    code: string;
    language: string;
}>();
</script>

<style scoped>
.hljs {
    border-radius: 0.5em;
}
</style>
