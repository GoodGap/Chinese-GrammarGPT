<script lang="ts" setup>
import { onMounted, reactive } from "vue";
import { useRouter, RouterLink } from "vue-router";
// example components
import DefaultNavbar from "@/examples/navbars/NavbarDefault.vue";
import Header from "@/examples/Header.vue";

// Vue Material Kit 2 components
import MaterialInput from "@/components/MaterialInput.vue";
import MaterialSwitch from "@/components/MaterialSwitch.vue";
import MaterialButton from "@/components/MaterialButton.vue";

// material-input
import setMaterialInput from "@/assets/js/material-input";

// server
import { User, userSignIn, ServerResponse, getUserDetail, UserDetail, emptyUser } from "@/server/user";

// store
import { useUserStore } from "@/stores/user"
const userStore = useUserStore()

const router = useRouter()


const user: User = reactive(emptyUser())


function onSignIn() {
  console.log(user)
  userSignIn(user).then(response => {
    let res: ServerResponse = response.data
    if (res.code == 0) {
      user.id = res.login_info.id
      user.token = res.login_info.token
      getUserDetail(user.username).then(response => {
        let res: ServerResponse = response.data
        if (res.code == 0) {
          let userDetail: UserDetail = res.data[0]
          if (userDetail) {
            userDetail.token = user.token
            userDetail.id = user.id
            userStore.userDetail = userDetail
            // setSessionUserDetail(userDetail)
            router.push({ path: "/" })
          }
        } else {
          alert(res.msg)
        }
      })
    } else {
      alert(res.msg)
    }
  }).catch(error => {
    console.log(error)
  })
}
onMounted(() => {
  setMaterialInput()
})

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
                    登录
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
                <form role="form" class="text-start" @submit.prevent="onSignIn">
                  <MaterialInput id="username" class="input-group-dynamic my-3" v-model="user.username"
                    :label="{ text: '用户名', class: 'form-label' }" type="text" />
                  <MaterialInput id="password" class="input-group-dynamic mb-3" v-model="user.password"
                    :label="{ text: '密码', class: 'form-label' }" type="password" />
                  <MaterialSwitch class="d-flex align-items-center mb-3" id="rememberMe" labelClass="mb-0 ms-3" checked>
                    记住我</MaterialSwitch>

                  <div class="text-center">
                    <MaterialButton class="my-4 mb-2" variant="gradient" color="success" fullWidth>
                      登录
                    </MaterialButton>
                  </div>

                  <p class="mt-4 text-sm text-center">
                    还没有账号?
                    <RouterLink to="signup" class="text-success text-gradient font-weight-bold">立即注册</RouterLink>
                  </p>
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
