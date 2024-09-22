<script setup lang="ts">
import { RouteLocationRaw, RouterLink } from 'vue-router';

defineProps<{
  image: string;
  title: string;
  description: string;
  action: {
    route: RouteLocationRaw;
    label: string;
    color: string;
  }[];
}>();

</script>
<template>
  <div class="back back-background" :style="{
    backgroundImage: `url(${image})`,
    backgroundSize: 'cover',
  }">
    <div class="card-body pt-7 text-center">
      <h3 class="text-white" v-html="title"></h3>
      <p class="text-white opacity-8">
        {{ description }}
      </p>
      <div class="buttons-group">

        <RouterLink v-for="({ route, color, label }, index) of action" :key="index" :to="route"
          class="btn btn-sm mt-3 inline-block ms-1" :class="`${color ? `btn-${color}` : 'btn-white'}`">{{ label }}
        </RouterLink>
      </div>
    </div>
  </div>
</template>
