<script setup lang="ts">
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";

//nav-pills
import guideImg1 from "@/assets/img/helper/guide_1.jpg"
import guideImg2 from "@/assets/img/helper/guide_2.png"
import guideImg3 from "@/assets/img/helper/guide_3.png"
import guideImg4 from "@/assets/img/helper/guide_4.jpg"
import guideImg5 from "@/assets/img/helper/guide_5.png"
import guideImg6 from "@/assets/img/helper/guide_6.png"
import guideImg7 from "@/assets/img/helper/guide_7.png"


</script>
<template>
  <BaseLayout title="用户指南" :breadcrumb="[{ label: '帮助文档', route: '#' }, { label: '用户指南' }]">
    <div class="position-relative border-radius-xl overflow-hidden shadow-lg mb-7 p-4">
      <p>项目部署的地址:http://222.20.95.251:4000/</p>
      <ol>
        <li>
          <p>输入上述网址，进入系统首页</p>
        </li>
      </ol>
      <p><img :src="guideImg1" class="w-80" loading="lazy" /></p>
      <ol start="2">
        <li>
          <p>点击登录，进入登录界面</p>
        </li>
      </ol>
      <p><img :src="guideImg2" class="w-80" loading="lazy" /></p>
      <ol start="3">
        <li>
          <p>第一次登录，请点击“立即注册”，跳转注册界面</p>
        </li>
      </ol>
      <p><img :src="guideImg3" class="w-80" loading="lazy" /></p>
      <ol start="4">
        <li>
          <p>点击“注册账号”，即可进入系统</p>
        </li>
      </ol>
      <p><img :src="guideImg4" class="w-80" loading="lazy" /></p>
      <ol start="5">
        <li>
          <p>点击右上角的个人头像，即可跳转输入界面</p>
        </li>
      </ol>
      <p><img :src="guideImg5" class="w-80" loading="lazy" /></p>
      <ol start="6">
        <li>
          <p>点击“文档”，然后点击“上传文件”</p>
        </li>
      </ol>
      <p><img :src="guideImg6" class="w-80" loading="lazy" /></p>
      <ol start="7">
        <li>
          <p>在输入框上传文件，点击编辑，等待文件修改结果即可</p>
        </li>
      </ol>
      <p><img :src="guideImg7" class="w-80" loading="lazy" /></p>
    </div>
  </BaseLayout>
</template>

<style scoped>
p {
  color: black;
  font-weight: normal;
}

ol {
  color: black;
  font-weight: bold;
}
</style>