<script lang="ts" setup>
import { onMounted, reactive, ref } from "vue";
import { useRouter } from "vue-router";
// example components
import DefaultNavbar from "@/examples/navbars/NavbarDefault.vue";
import Header from "@/examples/Header.vue";

//Vue Material Kit 2 components
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialButton from "@/components/MaterialButton.vue";

// material-input
import setMaterialInput from "@/assets/js/material-input";

// server
import {
  User, UserDetail, ServerResponse, userSignUp, userSignIn, emptyUserDetail
} from "@/server/user";

// store
import { useUserStore } from "@/stores/user"

const userStore = useUserStore();
const router = useRouter();
const userDetail: UserDetail = reactive(emptyUserDetail());

function onSignUp() {
  userSignUp(userDetail)
    .then(response => {
      console.log(response)
      if (response.data) {
        let serverRes: ServerResponse = response.data
        if (serverRes.code == 0) {
          console.log("sign up success")
          userSignIn({ username: userDetail.username, password: userDetail.password })
            .then(res => {
              if (res.data.code == 0) {
                let loginRes: ServerResponse = res.data
                let loginInfo = loginRes.login_info
                if (loginInfo) {
                  userDetail.id = loginInfo.id
                  userDetail.token = loginInfo.token
                  userStore.userDetail = userDetail
                  // setSessionUserDetail(userDetail)
                  router.push({ path: "/" })
                }
                router.push({ path: "/" })
              } else {
                alert("登录失败:" + res.data.msg)
              }
            })
        } else {
          alert(serverRes.msg)
        }
      }
    }).catch(err => console.log(err))
}

onMounted(() => {
  setMaterialInput();

});

</script>
<template>
  <DefaultNavbar transparent />
  <Header>
    <div class="page-header align-items-start min-vh-100" :style="{
      backgroundImage:
        'url(https://images.unsplash.com/photo-1497294815431-9365093b7331?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80)'
    }" loading="lazy">
      <span class="mask bg-gradient-dark opacity-6"></span>
      <div class="container my-auto">
        <div class="row">
          <div class="col-lg-4 col-md-8 col-12 mx-auto">
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                <div class="bg-gradient-success shadow-success border-radius-lg py-3 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">
                    注册
                  </h4>
                  <!-- <div class="row mt-3">
                    <div class="col-2 text-center ms-auto">
                      <a class="btn btn-link px-3" href="javascript:;">
                        <i class="fa fa-facebook text-white text-lg"></i>
                      </a>
                    </div>
                    <div class="col-2 text-center px-1">
                      <a class="btn btn-link px-3" href="javascript:;">
                        <i class="fa fa-github text-white text-lg"></i>
                      </a>
                    </div>
                    <div class="col-2 text-center me-auto">
                      <a class="btn btn-link px-3" href="javascript:;">
                        <i class="fa fa-google text-white text-lg"></i>
                      </a>
                    </div>
                  </div> -->
                </div>
              </div>
              <div class="card-body">
                <form role="form" class="text-start" @submit.prevent="onSignUp">
                  <MaterialInput id="username" class="input-group-dynamic my-3" v-model="userDetail.username"
                    :label="{ text: '用户名', class: 'form-label' }" type="text" :is-required="true" />
                  <MaterialInput id="email" class="input-group-dynamic my-3" v-model="userDetail.email"
                    :label="{ text: '邮箱', class: 'form-label' }" type="email" :is-required="true" />
                  <MaterialInput id="password" class="input-group-dynamic mb-3" v-model="userDetail.password"
                    :label="{ text: '密码', class: 'form-label' }" type="password" :is-required="true" />
                  <MaterialInput id="phone" class="input-group-dynamic mb-3" v-model="userDetail.telephone"
                    :label="{ text: '手机号', class: 'form-label' }" type="tel" pattern="^1[3,5,7,8]\d{9}$"
                    :is-required="true" />
                  <MaterialInput id="address" class="input-group-dynamic mb-3" v-model="userDetail.address"
                    :label="{ text: '地址', class: 'form-label' }" type="text" :is-required="true" />
                  <div class="text-center">
                    <MaterialButton class="my-4 mb-2" variant="gradient" color="success" fullWidth>注册账号
                    </MaterialButton>
                  </div>
                  <!-- <p class="mt-4 text-sm text-center">
                                        Don't have an account?
                                        <a href="#" class="text-success text-gradient font-weight-bold">Sign up</a>
                                    </p> -->
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- <footer class="footer position-absolute bottom-2 py-2 w-100">
        <div class="container">
          <div class="row align-items-center justify-content-lg-between">
            <div class="col-12 col-md-6 my-auto">
              <div class="copyright text-center text-sm text-white text-lg-start">
                © {{ new Date().getFullYear() }}, made with
                <i class="fa fa-heart" aria-hidden="true"></i> by
                <a href="https://www.creative-tim.com" class="font-weight-bold text-white" target="_blank">Creative
                  Tim</a>
                for a better web.
              </div>
            </div>
            <div class="col-12 col-md-6">
              <ul class="nav nav-footer justify-content-center justify-content-lg-end">
                <li class="nav-item">
                  <a href="https://www.creative-tim.com" class="nav-link text-white" target="_blank">Creative Tim</a>
                </li>
                <li class="nav-item">
                  <a href="https://www.creative-tim.com/presentation" class="nav-link text-white" target="_blank">About
                    Us</a>
                </li>
                <li class="nav-item">
                  <a href="https://www.creative-tim.com/blog" class="nav-link text-white" target="_blank">Blog</a>
                </li>
                <li class="nav-item">
                  <a href="https://www.creative-tim.com/license" class="nav-link pe-0 text-white"
                    target="_blank">License</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </footer> -->
    </div>
  </Header>
</template>
