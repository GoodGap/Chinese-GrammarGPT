<script setup>
import logoDark from "@/assets/img/logo-ct-dark.png";
import { RouterLink } from "vue-router";
defineProps({
  brand: {
    type: Object,
    name: String,
    logo: String,
    route: "",
    default: () => ({
      name: "智能纠错系统",
      logo: logoDark,
      route: "/"
    })
  },
  socials: {
    type: Array,
    icon: String,
    link: String,
    default: () => [
      {
        icon: '<i class="fab fa-qq text-lg opacity-8"></i>',
        link: "",
      },
      {
        icon: '<i class="fab fa-weixin text-lg opacity-8"></i>',
        link: "",
      },
      {
        icon: `<svg width="20px" height="20px" class="fab text-lg " xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true" data-testid="GiteeLogo" viewBox="120 13 72 72">
                <g fill="none" fill-rule="evenodd" transform="">
                  <path d="m0 0h312v100h-312z" />
                  <path
                    d="m156 85c-19.882251 0-36-16.117749-36-36s16.117749-36 36-36 36 16.117749 36 36-16.117749 36-36 36zm18.222232-39.9993426-20.444332.0004656c-.981652 0-1.777511.7956502-1.777768 1.7773025l-.002109 4.4442415c-.000258.9818341.795468 1.7779763 1.777302 1.7782335h.00048l12.446471-.0005988c.981834-.0000082 1.777775.795919 1.777783 1.7777532v.0000148l-.000015.4443924v.4444466c0 2.9455024-2.387801 5.3333039-5.333304 5.3333039l-16.890119-.000049c-.981693 0-1.77752-.7958052-1.777547-1.7774984l-.000662-16.8884814c-.000081-2.9455025 2.387655-5.3333698 5.333157-5.333451h.000147l24.885554-.0009559c.981404 0 1.777159-.795262 1.777768-1.7766654l.004962-4.4442409c.000609-.981834-.794831-1.7782613-1.776665-1.7788703-.000368-.0000002-.000735-.0000003-.001103-.0000003l-24.888752.0011758c-7.363727 0-13.333219 5.9694589-13.333259 13.3331863l-.000221 24.8878699c-.000005.9818342.795924 1.7777724 1.777758 1.7777778l26.222571-.0000098c6.627235 0 11.999671-5.3724358 11.999671-11.9996713v-10.2219033c0-.9818341-.795934-1.777768-1.777768-1.777768z"
                    fill="#c71d23" />
                </g>
              </svg>`,
        link: "https://gitee.com/GOODGAP/AutoThesisCorrection",
      },
    ]
  },
  menus: {
    type: Array,
    name: String,
    items: {
      type: Array,
      name: String,
      href: String
    },
    default: () => [
      {
        name: "项目介绍",
        items: [
          {
            name: "系统架构图",
            route: { name: "structure" }
          },
          {
            name: "Mindmap",
            route: { name: "mindmap" }
          },
          {
            name: "软件设计",
            route: { name: "design" }
          },
          {
            name: "NABCD分析",
            route: { name: "nabcd" }
          },
          {
            name: "团队成员",
            route: { name: "member" }
          }
        ]
      },
      {
        name: "帮助",
        items: [
          {
            name: "用户指南",
            route: { name: "guide" }
          },
          {
            name: "部署指南",
            route: { name: "deploy" }
          },
        ]
      },

    ]
  }
});
</script>
<template>
  <footer class="footer pt-5 mt-5">
    <div class="container">
      <div class="row">
        <div class="col-md-3 mb-4 ms-auto">
          <div>
            <a :href="brand.route">
              <img :src="brand.logo" class="mb-3 footer-logo" alt="main_logo" />
            </a>
            <h6 class="font-weight-bolder mb-4">{{ brand.name }}</h6>
          </div>
          <div>
            <ul class="d-flex flex-row ms-n3 nav">
              <li class="nav-item" v-for="{ icon, link } of socials" :key="link">
                <a class="nav-link pe-1" :href="link" target="_blank" v-html="icon">
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-md-2 col-sm-6 col-6 mb-4" v-for="{ name, items } of menus" :key="name">
          <h6 class="text-sm">{{ name }}</h6>
          <ul class="flex-column ms-n3 nav">
            <li class="nav-item" v-for="item of items" :key="item.name">
              <RouterLink class="nav-link" :to="item.route">
                {{ item.name }}
              </RouterLink>
            </li>
          </ul>
        </div>

        <!-- <div class="col-12">
          <div class="text-center">
            <p class="text-dark my-4 text-sm font-weight-normal">
              All rights reserved. Copyright ©
              {{ new Date().getFullYear() }}
              智能纠错系统 by
              <a href="https://www.creative-tim.com" target="_blank">xx团队</a>.
            </p>
          </div>
        </div> -->
      </div>
    </div>
  </footer>
</template>
