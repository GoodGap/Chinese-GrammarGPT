<script setup lang="ts">
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import Diagram from "@/assets/img/project/模型架构图.png"
</script>
<template>
  <BaseLayout title="系统结构图" :breadcrumb="[{ label: '图表', route: '#' }, { label: '系统结构图' }]">
    <div class="border-radius-xl overflow-hidden shadow-lg mb-7 p-4">
      <img :src="Diagram" alt="Mindmap" class="w-100" />
    </div>
  </BaseLayout>
</template>