<script lang="ts" setup>
import { computed, onMounted, onUnmounted, reactive, ref } from "vue";

//example components
import NavbarDefault from "../..//examples/navbars/NavbarDefault.vue";
import DefaultFooter from "../../examples/footers/FooterDefault.vue";
import Header from "../../examples/Header.vue";
import FilledInfoCard from "../../examples/cards/infoCards/FilledInfoCard.vue";

//Vue Material Kit 2 components
import MaterialSocialButton from "@/components/MaterialSocialButton.vue";

// sections
import PresentationCounter from "./Sections/PresentationCounter.vue";
import PresentationPages from "./Sections/PresentationPages.vue";
import PresentationExample from "./Sections/PresentationExample.vue";
import data from "./Sections/Data/designBlocksData";
import BuiltByDevelopers from "./Components/BuiltByDevelopers.vue";
import PresentationTestimonials from "./Sections/PresentationTestimonials.vue";
import PresentationInformation from "./Sections/PresentationInformation.vue";

//images
import vueMkHeader from "@/assets/img/vue-mk-header.jpg";
import wavesWhite from "@/assets/img/waves-white.svg";
import logoBootstrap from "@/assets/img/logos/bootstrap5.jpg";
import logoTailwind from "@/assets/img/logos/icon-tailwind.jpg";
import logoVue from "@/assets/img/logos/vue.jpg";
import logoAngular from "@/assets/img/logos/angular.jpg";
import logoReact from "@/assets/img/logos/react.jpg";
import logoSketch from "@/assets/img/logos/sketch.jpg";
import { UserDetail, emptyUserDetail, getSessionUserDetail } from "@/server/user";
import FooterCentered from "@/examples/footers/FooterCentered.vue";
import hustbg from "@/assets/img/hust/hustbg.png"
//hooks
const body = document.getElementsByTagName("body")[0];
const userDetail: UserDetail = reactive(getSessionUserDetail() ?? emptyUserDetail())
const showTitle = computed(() => userDetail.username != null && userDetail.username != "");

onMounted(() => {
  body.classList.add("presentation-page");
  body.classList.add("bg-gray-200");
});
onUnmounted(() => {
  body.classList.remove("presentation-page");
  body.classList.remove("bg-gray-200");
});
</script>

<template>
  <div class="container position-sticky z-index-sticky top-0">
    <div class="row">
      <div class="col-12">
        <NavbarDefault :sticky="true" />
      </div>
    </div>
  </div>
  <Header>
    <div class="page-header min-vh-75" loading="lazy" :style="{ backgroundImage: `url(${hustbg})` }">
      <div class="container">
        <div class="row">
          <div class="col-lg-7 text-center mx-auto position-relative">
            <h1 class="text-white pt-3 me-2" :style="{ display: 'inline-block ' }">
              大语言模型下的文本智能纠错
            </h1>
            <p class="lead text-white px-5 mt-6" :style="{ fontWeight: 500 }">
              本项目将从数据集、算法模型、纠错系统三方面入手实施，计划基于大语言模型(LLM)的强推理能力和云计算的高性能计算能力构建出一个学术论文智能纠错系统。
            </p>
          </div>
        </div>
      </div>
    </div>
  </Header>

  <div class="card card-body blur shadow-blur mx-3 mx-md-4 mt-n6">
    <PresentationCounter />
    <PresentationInformation />
    <PresentationExample :data="data" />
    <!-- <PresentationPages /> -->
    <!-- <BuiltByDevelopers /> -->

    <!-- <div class="container">
      <div class="row">
        <div class="col-lg-4">
          <FilledInfoCard class="p-4" :color="{ text: 'white', background: 'bg-gradient-success' }"
            :icon="{ component: 'flag', color: 'white' }" title="Getting Started"
            description="Check the possible ways of working with our product and the necessary files for building your own project."
            :action="{
              route:
                'https://www.creative-tim.com/learning-lab/vue/overview/material-kit/',
              label: { text: 'Let\'s start', color: 'white' }
            }" />
        </div>
        <div class="col-lg-4">
          <FilledInfoCard class="px-lg-1 mt-lg-0 mt-4 p-4" height="h-100"
            :icon="{ component: 'precision_manufacturing', color: 'success' }" title="Plugins" description="Get inspiration and have an overview about the plugins that we
                used to create the Material Kit." :action="{
                  route:
                    'https://www.creative-tim.com/learning-lab/vue/input/material-kit/',
                  label: { text: 'Read more' }
                }" />
        </div>
        <div class="col-lg-4">
          <FilledInfoCard class="px-lg-1 mt-lg-0 mt-4 p-4" :icon="{ component: 'receipt_long', color: 'success' }"
            title="Utility Classes" description="Material Kit is giving you a lot of pre-made elements. For those
                who want flexibility, we included many utility classes." :action="{
                  route:
                    'https://www.creative-tim.com/learning-lab/vue/utilities/material-kit/',
                  label: { text: 'Read more' }
                }" />
        </div>
      </div>
    </div> -->
    <!-- <PresentationTestimonials /> -->

    <!-- <div class="container-fluid mt-sm-5 border-radius-xl" :style="{
      background: 'linear-gradient(195deg, rgb(66, 66, 74), rgb(25, 25, 25))'
    }">
      <div class="page-header py-6 py-md-5 my-sm-3 mb-3 border-radius-xl" :style="{
        backgroundImage: `url(${wavesWhite})`
      }" loading="lazy">
        <span class="mask bg-gradient-dark"></span>
        <div class="container">
          <div class="row">
            <div class="d-flex justify-content-center p-5">
              <div class="col-lg-8 ms-lg-5 text-center">
                <h3 class="text-white">
                  Do you love this awesome UI Kit from Vuejs & Bootstrap?
                </h3>
                <p class="text-white text-md">
                  Cause if you do, it can be yours for FREE. Hit the button
                  below to navigate to Creative Tim where you can <br />
                  find the Design System in HTML. Start a new project or give an
                  old Bootstrap project a new look!
                </p>

                <a href="https://www.creative-tim.com/product/vue-material-kit"
                  class="btn btn-sm mb-0 bg-gradient-success px-5 py-3 mt-4">Download Now</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> -->

    <!-- <div class="container">
      <div class="row">
        <div class="d-flex flex-column w-100 text-center p-5 mb-8">
          <h3>Available on these technologies</h3>
          <div class="d-flex justify-content-center mt-3 flex-wrap">
            <a href="https://www.creative-tim.com/product/material-kit" data-bs-toggle="tooltip"
              data-bs-placement="bottom" title="Bootstrap 5 - Most popular front-end component library">
              <img :src="logoBootstrap" alt="title" loading="lazy" :style="{ height: '90px' }" />
            </a>
            <a class="opacity-5 ms-3" href="#" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Coming Soon">
              <img :src="logoTailwind" alt="title" loading="lazy" :style="{ height: '90px' }" />
            </a>
            <a href="https://www.creative-tim.com/product/vue-material-kit-pro" class="mx-3" data-bs-toggle="tooltip"
              data-bs-placement="bottom" title="Vue.js - Is a Progressive JavaScript Framework">
              <img :src="logoVue" alt="title" loading="lazy" :style="{ height: '90px' }" />
            </a>
            <a class="opacity-5" href="#" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Coming Soon">
              <img :src="logoAngular" alt="title" loading="lazy" :style="{ height: '90px' }" />
            </a>
            <a href="https://www.creative-tim.com/product/material-kit-react-pro" class="mx-3" data-bs-toggle="tooltip"
              data-bs-placement="bottom" title="React – A JavaScript library for building user interfaces">
              <img :src="logoReact" alt="title" loading="lazy" :style="{ height: '90px' }" />
            </a>
            <a class="opacity-5" href="#" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Coming Soon">
              <img :src="logoSketch" alt="title" loading="lazy" :style="{ height: '90px' }" />
            </a>
          </div>
        </div>
      </div>
    </div> -->
    <!-- <div class="py-5">
      <div class="container">
        <div class="row">
          <div class="col-lg-5 ms-auto">
            <h4 class="mb-1">Thank you for your support!</h4>
            <p class="lead mb-0">We deliver the best web products</p>
          </div>
          <div class="col-lg-5 me-lg-auto my-lg-auto text-lg-end mt-5">
            <MaterialSocialButton
              route="https://twitter.com/intent/tweet?text=Check%20Material%20Design%20System%20made%20by%20%40CreativeTim%20%23webdesign%20%23designsystem%20%23bootstrap5&url=https%3A%2F%2Fwww.creative-tim.com%2Fproduct%2Fmaterial-design-system-pro"
              component="twitter" color="twitter" label="Tweet" />
            <MaterialSocialButton
              route="https://www.facebook.com/sharer/sharer.php?u=https://www.creative-tim.com/product/material-design-system-pro"
              component="facebook-square" color="facebook" label="Share" />
            <MaterialSocialButton route="" component="pinterest" color="pinterest" label="Pin it" />
          </div>
        </div>
      </div>
    </div> -->
  </div>
  <DefaultFooter />
  <!-- <FooterCentered /> -->
</template>
