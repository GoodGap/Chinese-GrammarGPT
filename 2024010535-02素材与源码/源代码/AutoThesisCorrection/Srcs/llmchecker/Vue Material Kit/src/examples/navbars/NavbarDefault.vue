<script setup lang="ts">
import { RouterLink } from "vue-router";
import { onMounted, reactive, ref, watch } from "vue";
import { useWindowsWidth } from "../../assets/js/useWindowsWidth";

// images
import ArrDark from "@/assets/img/down-arrow-dark.svg";
import downArrow from "@/assets/img/down-arrow.svg";
import DownArrWhite from "@/assets/img/down-arrow-white.svg";
import GiteeLogo from "@/assets/img/logos/gitee.svg"
import { useUserStore } from "@/stores/user";
import { storeToRefs } from "pinia";
const userStore = useUserStore();
const userDetail = storeToRefs(userStore).userDetail;
const props = defineProps({
  action: {
    type: Object,
    route: String,
    color: String,
    label: String,
    default: () => ({
      route: { name: "signin" },
      color: "bg-gradient-success",
      label: "登录"
    })
  },
  transparent: {
    type: Boolean,
    default: false
  },
  light: {
    type: Boolean,
    default: false
  },
  dark: {
    type: Boolean,
    default: false
  },
  sticky: {
    type: Boolean,
    default: false
  },
  darkText: {
    type: Boolean,
    default: false
  }
});

// set arrow  color
function getArrowColor() {
  if (props.transparent && textDark.value) {
    return ArrDark;
  } else if (props.transparent) {
    return DownArrWhite;
  } else {
    return ArrDark;
  }
}

// set text color
const getTextColor = () => {
  let color;
  if (props.transparent && textDark.value) {
    color = "text-dark";
  } else if (props.transparent) {
    color = "text-white";
  } else {
    color = "text-dark";
  }

  return color;
};

// set nav color on mobile && desktop

let textDark = ref(props.darkText);
const { type } = useWindowsWidth();


if (type.value === "mobile") {
  textDark.value = true;
} else if (type.value === "desktop" && textDark.value == false) {
  textDark.value = false;
}

watch(
  () => type.value,
  (newValue) => {
    if (newValue === "mobile") {
      textDark.value = true;
    } else {
      textDark.value = false;
    }
  }
);
</script>
<template>
  <nav class="navbar navbar-expand-lg top-0" :class="{
    'z-index-3 w-100 shadow-none navbar-transparent position-absolute my-3':
      props.transparent,
    'my-3 blur border-radius-lg z-index-3 py-2 shadow py-2 start-0 end-0 mx-4 position-absolute mt-4':
      props.sticky,
    'navbar-light bg-white py-3': props.light,
    ' navbar-dark bg-gradient-dark z-index-3 py-3': props.dark
  }">
    <div :class="props.transparent || props.light || props.dark
      ? 'container'
      : 'container-fluid px-0'
      ">
      <RouterLink class="navbar-brand d-none d-md-block" :class="[
        (props.transparent && textDark) || !props.transparent
          ? 'text-dark font-weight-bolder ms-sm-3'
          : 'text-white font-weight-bolder ms-sm-3'
      ]" to="/" rel="tooltip" title="跳转主页" data-placement="bottom">
        智能纠错系统
      </RouterLink>
      <RouterLink class="navbar-brand d-block d-md-none" :class="props.transparent || props.dark
        ? 'text-white'
        : 'font-weight-bolder ms-sm-3'
        " to="/" rel="tooltip" title="跳转主页" data-placement="bottom">
        智能纠错系统
      </RouterLink>
      <RouterLink :to="{ name: 'profile' }" class="mb-0 ms-auto d-lg-none d-block" v-if="userStore.isLogin" title="我的信息">
        <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24px" viewBox="0 0 24 24"
          width="24px" :fill="props.transparent ? '#fff' : '#666666'">
          <g>
            <rect fill="none" height="24" width="24" />
          </g>
          <g>
            <path
              d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 4c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm0 14c-2.03 0-4.43-.82-6.14-2.88C7.55 15.8 9.68 15 12 15s4.45.8 6.14 2.12C16.43 19.18 14.03 20 12 20z" />
          </g>
        </svg>
      </RouterLink>
      <RouterLink :to="action.route" class="btn btn-sm bg-gradient-success mb-0 ms-auto d-lg-none d-block"
        :class="action.color" v-else>
        登录
      </RouterLink>
      <button class="navbar-toggler shadow-none ms-2" type="button" data-bs-toggle="collapse" data-bs-target="#navigation"
        aria-controls="navigation" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon mt-2">
          <span class="navbar-toggler-bar bar1"></span>
          <span class="navbar-toggler-bar bar2"></span>
          <span class="navbar-toggler-bar bar3"></span>
        </span>
      </button>
      <div class="collapse navbar-collapse w-100 pt-3 pb-2 py-lg-0" id="navigation">
        <ul class="navbar-nav navbar-nav-hover ms-auto">
          <!-- <li class="nav-item dropdown dropdown-hover mx-2">
            <a role="button" class="nav-link ps-2 d-flex cursor-pointer align-items-center" :class="getTextColor()"
              id="dropdownMenuPages" data-bs-toggle="dropdown" aria-expanded="false">
              <i class="material-icons opacity-6 me-2 text-md" :class="getTextColor()">dashboard</i>
              Pages
              <img :src="getArrowColor()" alt="down-arrow" class="arrow ms-2 d-lg-block d-none" />
              <img :src="getArrowColor()" alt="down-arrow" class="arrow ms-1 d-lg-none d-block ms-auto" />
            </a>
            <div class="dropdown-menu dropdown-menu-animation ms-n3 dropdown-md p-3 border-radius-xl mt-0 mt-lg-3"
              aria-labelledby="dropdownMenuPages">
              <div class="row d-none d-lg-block">
                <div class="col-12 px-4 py-2">
                  <div class="row">
                    <div class="position-relative">
                      <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-1">
                        Landing Pages
                      </div>
                      <RouterLink :to="{ name: 'about' }" class="dropdown-item border-radius-md">
                        <span>About Us</span>
                      </RouterLink>
                      <RouterLink :to="{ name: 'contactus' }" class="dropdown-item border-radius-md">
                        <span>Contact Us</span>
                      </RouterLink>
                      <RouterLink :to="{ name: 'author' }" class="dropdown-item border-radius-md">
                        <span>Author</span>
                      </RouterLink>
                      <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-0 mt-3">
                        Account
                      </div>
                      <RouterLink :to="{ name: 'signin' }" class="dropdown-item border-radius-md">
                        <span>Sign In</span>
                      </RouterLink>
                    </div>
                  </div>
                </div>
              </div>
              <div class="d-lg-none">
                <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-0">
                  Landing Pages
                </div>
                <RouterLink :to="{ name: 'about' }" class="dropdown-item border-radius-md">
                  <span>About Us</span>
                </RouterLink>
                <RouterLink :to="{ name: 'contactus' }" class="dropdown-item border-radius-md">
                  <span>Contact Us</span>
                </RouterLink>
                <RouterLink :to="{ name: 'author' }" class="dropdown-item border-radius-md">
                  <span>Author</span>
                </RouterLink>
                <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-0 mt-3">
                  Account
                </div>
                <RouterLink :to="{ name: 'signin' }" class="dropdown-item border-radius-md">
                  <span>Sign In</span>
                </RouterLink>
              </div>
            </div>
          </li> -->
          <li class="nav-item dropdown dropdown-hover mx-2">
            <a role="button" class="nav-link ps-2 d-flex cursor-pointer align-items-center" :class="getTextColor()"
              id="dropdownMenuBlocks" data-bs-toggle="dropdown" aria-expanded="false">
              <i class="material-icons opacity-6 me-2 text-md" :class="getTextColor()">view_day</i>
              项目介绍
              <img :src="getArrowColor()" alt="down-arrow" class="arrow ms-2 d-lg-block d-none" />
              <img :src="getArrowColor()" alt="down-arrow" class="arrow ms-1 d-lg-none d-block ms-auto" />
            </a>
            <div
              class="dropdown-menu dropdown-menu-end dropdown-menu-animation dropdown-md dropdown-md-responsive p-3 border-radius-lg mt-0 mt-lg-3"
              aria-labelledby="dropdownMenuBlocks">
              <div class="d-none d-lg-block">
                <ul class="list-group">
                  <li class="nav-item dropdown dropdown-hover dropdown-subitem list-group-item border-0 p-0">
                    <a class="dropdown-item py-2 ps-3 border-radius-md" href="javascript:;">
                      <div class="d-flex">
                        <div class="w-100 d-flex align-items-center justify-content-between">
                          <div>
                            <h6
                              class="dropdown-header text-dark font-weight-bolder d-flex justify-content-cente align-items-center p-0">
                              项目图表
                            </h6>
                            <span class="text-sm">项目相关图表</span>
                          </div>
                          <img :src="downArrow" alt="down-arrow" class="arrow" />
                        </div>
                      </div>
                    </a>
                    <div class="dropdown-menu mt-0 py-3 px-2 mt-3">
                      <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'structure' }">
                        系统架构图
                      </RouterLink>
                      <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'mindmap' }">
                        Mindmap
                      </RouterLink>
                    </div>
                  </li>
                  <li class="nav-item dropdown dropdown-hover dropdown-subitem list-group-item border-0 p-0">
                    <a class="dropdown-item py-2 ps-3 border-radius-md" href="javascript:;">
                      <div class="d-flex">
                        <div class="w-100 d-flex align-items-center justify-content-between">
                          <div>
                            <h6
                              class="dropdown-header text-dark font-weight-bolder d-flex justify-content-cente align-items-center p-0">
                              项目文档
                            </h6>
                            <span class="text-sm">查看项目相关信息</span>
                          </div>
                          <img :src="downArrow" alt="down-arrow" class="arrow" />
                        </div>
                      </div>
                    </a>
                    <div class="dropdown-menu mt-0 py-3 px-2 mt-3">
                      <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'design' }">
                        软件设计
                      </RouterLink>
                      <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'nabcd' }">
                        NABCD分析
                      </RouterLink>
                      <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'member' }">
                        团队成员
                      </RouterLink>
                    </div>
                  </li>
                </ul>
              </div>
              <div class="row d-lg-none">
                <div class="col-md-12">
                  <div class="d-flex mb-2">
                    <div class="w-100 d-flex align-items-center justify-content-between">
                      <div>
                        <h6
                          class="dropdown-header text-dark font-weight-bolder d-flex justify-content-cente align-items-center p-0">
                          项目图表
                        </h6>
                      </div>
                    </div>
                  </div>
                  <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'structure' }">
                    系统架构图
                  </RouterLink>
                  <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'mindmap' }">
                    Mindmap
                  </RouterLink>
                  <div class="d-flex mb-2 mt-3">
                    <div class="w-100 d-flex align-items-center justify-content-between">
                      <div>
                        <h6
                          class="dropdown-header text-dark font-weight-bolder d-flex justify-content-cente align-items-center p-0">
                          项目文档
                        </h6>
                      </div>
                    </div>
                  </div>
                  <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'design' }">
                    软件设计
                  </RouterLink>
                  <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'nabcd' }">
                    NABCD分析
                  </RouterLink>
                  <RouterLink class="dropdown-item ps-3 border-radius-md mb-1" :to="{ name: 'member' }">
                    团队成员
                  </RouterLink>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item dropdown dropdown-hover mx-2">
            <a role="button" class="nav-link ps-2 d-flex cursor-pointer align-items-center" :class="getTextColor()"
              id="dropdownMenuDocs" data-bs-toggle="dropdown" aria-expanded="false">
              <i class="material-icons opacity-6 me-2 text-md" :class="getTextColor()">article</i>
              帮助
              <img :src="getArrowColor()" alt="down-arrow" class="arrow ms-2 d-lg-block d-none" />
              <img :src="getArrowColor()" alt="down-arrow" class="arrow ms-1 d-lg-none d-block ms-auto" />
            </a>
            <div
              class="dropdown-menu dropdown-menu-end dropdown-menu-animation dropdown-md mt-0 mt-lg-3 p-3 border-radius-lg"
              aria-labelledby="dropdownMenuDocs">
              <div class="d-none d-lg-block">
                <ul class="list-group">
                  <li class="nav-item list-group-item border-0 p-0">
                    <RouterLink class="dropdown-item py-2 ps-3 border-radius-md" :to="{ name: 'guide' }">
                      <h6
                        class="dropdown-header text-dark font-weight-bolder d-flex justify-content-cente align-items-center p-0">
                        用户指南
                      </h6>
                      <span class="text-sm">快速上手智能纠错系统</span>
                    </RouterLink>
                  </li>
                  <li class="nav-item list-group-item border-0 p-0">
                    <RouterLink class="dropdown-item py-2 ps-3 border-radius-md" :to="{ name: 'deploy' }">
                      <h6
                        class="dropdown-header text-dark font-weight-bolder d-flex justify-content-cente align-items-center p-0">
                        部署指南
                      </h6>
                      <span class="text-sm">部署在你的服务器上</span>
                    </RouterLink>
                  </li>
                </ul>
              </div>
              <div class="row d-lg-none">
                <div class="col-md-12 g-0">
                  <RouterLink class="dropdown-item py-2 ps-3 border-radius-md" :to="{ name: 'guide' }">
                    <h6
                      class="dropdown-header text-dark font-weight-bolder d-flex justify-content-cente align-items-center p-0">
                      用户指南
                    </h6>
                    <span class="text-sm">快速上手智能纠错系统</span>
                  </RouterLink>
                  <RouterLink class="dropdown-item py-2 ps-3 border-radius-md" :to="{ name: 'deploy' }">
                    <h6
                      class="dropdown-header text-dark font-weight-bolder d-flex justify-content-cente align-items-center p-0">
                      部署指南
                    </h6>
                    <span class="text-sm">部署在你的服务器上</span>
                  </RouterLink>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item dropdown dropdown-hover mx-2">
            <a href="https://gitee.com/GOODGAP/AutoThesisCorrection"
              class="nav-link d-flex cursor-pointer align-items-center">
              <!-- gitee logo -->
              <svg width="20px" height="20px" class="material-icons me-2 " xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true" data-testid="GiteeLogo" viewBox="120 13 72 72">
                <g fill="none" fill-rule="evenodd" transform="">
                  <path d="m0 0h312v100h-312z" />
                  <path
                    d="m156 85c-19.882251 0-36-16.117749-36-36s16.117749-36 36-36 36 16.117749 36 36-16.117749 36-36 36zm18.222232-39.9993426-20.444332.0004656c-.981652 0-1.777511.7956502-1.777768 1.7773025l-.002109 4.4442415c-.000258.9818341.795468 1.7779763 1.777302 1.7782335h.00048l12.446471-.0005988c.981834-.0000082 1.777775.795919 1.777783 1.7777532v.0000148l-.000015.4443924v.4444466c0 2.9455024-2.387801 5.3333039-5.333304 5.3333039l-16.890119-.000049c-.981693 0-1.77752-.7958052-1.777547-1.7774984l-.000662-16.8884814c-.000081-2.9455025 2.387655-5.3333698 5.333157-5.333451h.000147l24.885554-.0009559c.981404 0 1.777159-.795262 1.777768-1.7766654l.004962-4.4442409c.000609-.981834-.794831-1.7782613-1.776665-1.7788703-.000368-.0000002-.000735-.0000003-.001103-.0000003l-24.888752.0011758c-7.363727 0-13.333219 5.9694589-13.333259 13.3331863l-.000221 24.8878699c-.000005.9818342.795924 1.7777724 1.777758 1.7777778l26.222571-.0000098c6.627235 0 11.999671-5.3724358 11.999671-11.9996713v-10.2219033c0-.9818341-.795934-1.777768-1.777768-1.777768z"
                    fill="#c71d23" />
                </g>
              </svg>
              Gitee
            </a>
          </li>
        </ul>
        <ul class="navbar-nav d-lg-block d-none">
          <li class="nav-item dropdown dropdown-hover mx-2">
            <!-- 用户头像 -->
            <div class="nav-link d-flex cursor-pointer align-items-center me-3" data-toggle="dropdown"
              aria-expanded="false" v-if="userStore.isLogin">
              <svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24px" viewBox="0 0 24 24"
                width="24px" :fill="props.transparent ? '#fff' : '#666666'">
                <g>
                  <rect fill="none" height="24" width="24" />
                </g>
                <g>
                  <path
                    d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 4c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm0 14c-2.03 0-4.43-.82-6.14-2.88C7.55 15.8 9.68 15 12 15s4.45.8 6.14 2.12C16.43 19.18 14.03 20 12 20z" />
                </g>
              </svg>
            </div>
            <!-- 登录按钮 -->
            <RouterLink :to="action.route" class="btn btn-sm mb-0 me-3" :class="action.color" v-else>
              登录
            </RouterLink>

            <!-- 用户下拉菜单 -->
            <div class="dropdown-menu dropdown-menu-animation ms-n3 p-3 border-radius-xl mt-0 mt-lg-3"
              v-if="userStore.isLogin" aria-labelledby="dropdownMenuPages">
              <div class="row d-none d-lg-block">
                <div class="col-12 px-2 py-1">
                  <div class="row">
                    <div class="position-relative">
                      <!-- <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-0 mt-3">
                        Editor
                      </div> -->
                      <RouterLink :to="{ name: 'profile' }" class="dropdown-item border-radius-md">
                        <span>我的信息</span>
                      </RouterLink>
                      <RouterLink :to="{ name: 'document' }" class="dropdown-item border-radius-md">
                        <span>我的文档</span>
                      </RouterLink>
                    </div>
                  </div>
                </div>
              </div>
              <!-- 小屏幕时显示 -->
              <div class="d-lg-none">
                <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-0">
                  Landing Pages
                </div>
                <RouterLink :to="{ name: 'about' }" class="dropdown-item border-radius-md">
                  <span>About Us</span>
                </RouterLink>
                <RouterLink :to="{ name: 'contactus' }" class="dropdown-item border-radius-md">
                  <span>Contact Us</span>
                </RouterLink>
                <RouterLink :to="{ name: 'author' }" class="dropdown-item border-radius-md">
                  <span>Author</span>
                </RouterLink>
                <div class="dropdown-header text-dark font-weight-bolder d-flex align-items-center px-0 mt-3">
                  Account
                </div>
                <RouterLink :to="{ name: 'signin' }" class="dropdown-item border-radius-md">
                  <span>Sign In</span>
                </RouterLink>
              </div>
            </div>


          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!-- End Navbar -->
</template>
