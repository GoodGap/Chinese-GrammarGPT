<script setup lang="ts">
import { reactive, onMounted } from "vue";
import { RouterView, RouterLink, useRouter } from "vue-router";
// Vue Material Kit
import DefaultNavbar from "@/examples/navbars/NavbarDefault.vue";
import DefaultFooter from "@/examples/footers/FooterDefault.vue";

onMounted(() => {

});

</script>

<template>
  <DefaultNavbar :action="{
    route: 'javascript:;',
    color: 'btn-white',
  }" transparent />
  <header class="bg-gradient-dark">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-8 text-center mx-auto my-6">
          <!-- <h1 class="text-white mb-6 mt-5">
            我的账户
          </h1> -->
        </div>
      </div>
    </div>

  </header>
  <div class="card card-body shadow-xl mx-8 mt-n5 account-info">
    <div class="container">
      <div class="row">
        <div class="col-2 text-center">
          <nav id="sidebarMenu" class="h-100 flex-column align-items-stretch pe-4 border-end">
            <div class="position-sticky">
              <div class="list-group list-group-flush mx-2">
                <RouterLink :to="{ name: 'profile' }" replace class="list-group-item list-group-item-action py-2"
                  :class="{ active: $router.currentRoute.value.name == 'profile' }">
                  信息
                </RouterLink>
                <RouterLink :to="{ name: 'document' }" replace class="list-group-item list-group-item-action py-2"
                  :class="{ active: $router.currentRoute.value.name == 'document' }">
                  文档
                </RouterLink>
                <a :to="{ name: 'setting' }" replace class="list-group-item list-group-item-action py-2">
                  <!-- TODO setting page -->
                  设置
                </a>
              </div>
            </div>
          </nav>
        </div>
        <div class="col-10">
          <RouterView />
        </div>
      </div>
    </div>
  </div>
  <div class="mb-6" />
</template>

<style scoped>
.account-info {
  min-height: 720px;
}
</style>