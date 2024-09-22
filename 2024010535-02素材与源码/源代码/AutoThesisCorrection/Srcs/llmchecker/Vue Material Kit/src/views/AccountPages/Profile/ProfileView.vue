<script setup lang="ts">
import { useUserStore } from '@/stores/user';
import { reactive, ref } from 'vue';

const userStore = useUserStore();
const userDetial = ref(userStore.userDetail);

</script>
<template>
  <div>
    <h2>账号信息</h2>
    <div class="container w-100">
      <div class="row mt-4">
        <div class="col-2">
          电子邮箱
        </div>
        <div class="col-8">
          {{ userDetial.email }}
        </div>
        <div class="col-2">
          <i class="bi bi-pencil-square"></i>
          编辑
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-2">
          用户名
        </div>
        <div class="col-8">
          {{ userDetial.username }}
        </div>
        <div class="col-2">
          <i class="bi bi-pencil-square"></i>
          编辑
        </div>
      </div>
      <div class="row mt-4">
        <div class="col-2">
          手机号
        </div>
        <div class="col-8">
          {{ userDetial.telephone }}
        </div>
        <div class="col-2">
          <i class="bi bi-pencil-square"></i>
          编辑
        </div>
      </div>
    </div>
  </div>
</template>