<script setup lang="ts">
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";
import Mindmap from "@/assets/img//project/mindmap.jpg";
import ExampleCard from "@/views/Presentation/Components/ExampleCard.vue";


</script>
<template>
  <BaseLayout title="Mindmap" :breadcrumb="[{ label: '图表', route: '#' }, { label: 'Mindmap' }]">
    <div class="border-radius-xl overflow-hidden shadow-lg mb-7 p-4">
      <img :src="Mindmap" alt="Mindmap" class="w-100" />
    </div>
  </BaseLayout>
</template>