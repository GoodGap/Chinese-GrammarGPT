import { createRouter, createWebHistory } from "vue-router";
import PresentationView from "../views/Presentation/PresentationView.vue";
import AboutView from "../views/LandingPages/AboutUs/AboutView.vue";
import ContactView from "../views/LandingPages/ContactUs/ContactView.vue";
import AuthorView from "../views/LandingPages/Author/AuthorView.vue";
import PageHeaders from "../layouts/sections/page-sections/page-headers/HeadersView.vue";
import PageFeatures from "../layouts/sections/page-sections/features/FeaturesView.vue";
import NavigationNavbars from "../layouts/sections/navigation/navbars/NavbarsView.vue";
import NavigationNavTabs from "../layouts/sections/navigation/nav-tabs/NavTabsView.vue";
import NavigationPagination from "../layouts/sections/navigation/pagination/PaginationView.vue";
import InputAreasInputs from "../layouts/sections/input-areas/inputs/InputsView.vue";
import InputAreasForms from "../layouts/sections/input-areas/forms/FormsView.vue";
import ACAlerts from "../layouts/sections/attention-catchers/alerts/AlertsView.vue";
import ACModals from "../layouts/sections/attention-catchers/modals/ModalsView.vue";
import ACTooltipsPopovers from "../layouts/sections/attention-catchers/tooltips-popovers/TooltipsPopoversView.vue";
import ElAvatars from "../layouts/sections/elements/avatars/AvatarsView.vue";
import ElBadges from "../layouts/sections/elements/badges/BadgesView.vue";
import ElBreadcrumbs from "../layouts/sections/elements/breadcrumbs/BreadcrumbsView.vue";
import ElButtons from "../layouts/sections/elements/buttons/ButtonsView.vue";
import ElButtonGroups from "../layouts/sections/elements/button-groups/ButtonGroupsView.vue";
import ElDropdowns from "../layouts/sections/elements/dropdowns/DropdownsView.vue";
import ElProgressBars from "../layouts/sections/elements/progress-bars/ProgressBarsView.vue";
import ElToggles from "../layouts/sections/elements/toggles/TogglesView.vue";
import ElTypography from "../layouts/sections/elements/typography/TypographyView.vue";
import SignInView from "@/views/AccountPages/SignIn/SignInView.vue";
import SignUpView from "@/views/AccountPages/SignIn/SignUpView.vue";
import TiptapEditorView from "@/views/EditorPages/TiptapView.vue";
import AccountView from '@/views/AccountPages/AccountView.vue';
import ProfileView from "@/views/AccountPages/Profile/ProfileView.vue";
import DocumentView from "@/views/AccountPages/Document/DocumentView.vue";
import TestPage from "@/views/TestPage.vue";
import NotFoundPage from "@/views/NotFoundPage/NotFoundPage.vue";
import { getSessionUserDetail } from "@/server/user";
import GuideView from "@/views/HelperPages/GuideView.vue";
import DeployView from "@/views/HelperPages/DeployView.vue";
import MindmapView from "@/views/ProjectPages/Diagram/MindmapView.vue";
import StructureView from "@/views/ProjectPages/Diagram/StructureView.vue";
import DesignView from "@/views/ProjectPages/Docs/DesignView.vue";
import MemberView from "@/views/ProjectPages/Docs/MemberView.vue";
import NABCDView from "@/views/ProjectPages/Docs/NABCDView.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/test",
      name: "test",
      component: TestPage,
    },
    {
      path: "/",
      name: "presentation",
      component: PresentationView,
    },
    {
      path: "/editor/:filename",
      name: "tiptap-editor",
      component: TiptapEditorView,
    },
    {
      path: "/pages/landing-pages/about-us",
      name: "about",
      component: AboutView,
    },
    {
      path: "/pages/landing-pages/contact-us",
      name: "contactus",
      component: ContactView,
    },
    {
      path: "/pages/landing-pages/author",
      name: "author",
      component: AuthorView,
    },
    {
      path: "/account",
      name: "account",
      component: AccountView,
      children: [
        {
          path: "profile",
          name: "profile",
          component: ProfileView
        },
        {
          path: "document",
          name: "document",
          component: DocumentView
        },
        {
          path: "",
          redirect: { name: "profile" },
        },
      ]
    },
    {
      path: "/project/diagram/mindmap",
      name: "mindmap",
      component: MindmapView,
    },
    {
      path: "/project/diagram/structure",
      name: "structure",
      component: StructureView,
    },
    {
      path: "/project/docs/design",
      name: "design",
      component: DesignView,
    },
    {
      path: "/project/docs/member",
      name: "member",
      component: MemberView,
    },
    {
      path: "/project/docs/nabcd",
      name: "nabcd",
      component: NABCDView,
    },
    {
      path: "/help/guide",
      name: "guide",
      component: GuideView,
    },
    {
      path: "/help/deploy",
      name: "deploy",
      component: DeployView
    },
    {
      path: "/signin",
      name: "signin",
      component: SignInView
    },
    {
      path: "/signup",
      name: "signup",
      component: SignUpView
    },
    {
      path: "/sections/page-sections/page-headers",
      name: "page-headers",
      component: PageHeaders,
    },
    {
      path: "/sections/page-sections/features",
      name: "page-features",
      component: PageFeatures,
    },
    {
      path: "/sections/navigation/navbars",
      name: "navigation-navbars",
      component: NavigationNavbars,
    },
    {
      path: "/sections/navigation/nav-tabs",
      name: "navigation-navtabs",
      component: NavigationNavTabs,
    },
    {
      path: "/sections/navigation/pagination",
      name: "navigation-pagination",
      component: NavigationPagination,
    },
    {
      path: "/sections/input-areas/inputs",
      name: "inputareas-inputs",
      component: InputAreasInputs,
    },
    {
      path: "/sections/input-areas/forms",
      name: "inputareas-forms",
      component: InputAreasForms,
    },
    {
      path: "/sections/attention-catchers/alerts",
      name: "ac-alerts",
      component: ACAlerts,
    },
    {
      path: "/sections/attention-catchers/modals",
      name: "ac-modals",
      component: ACModals,
    },
    {
      path: "/sections/attention-catchers/tooltips-popovers",
      name: "ac-tooltips-popovers",
      component: ACTooltipsPopovers,
    },
    {
      path: "/sections/elements/avatars",
      name: "el-avatars",
      component: ElAvatars,
    },
    {
      path: "/sections/elements/badges",
      name: "el-badges",
      component: ElBadges,
    },
    {
      path: "/sections/elements/breadcrumbs",
      name: "el-breadcrumbs",
      component: ElBreadcrumbs,
    },
    {
      path: "/sections/elements/buttons",
      name: "el-buttons",
      component: ElButtons,
    },
    {
      path: "/sections/elements/button-groups",
      name: "el-button-groups",
      component: ElButtonGroups,
    },
    {
      path: "/sections/elements/dropdowns",
      name: "el-dropdowns",
      component: ElDropdowns,
    },
    {
      path: "/sections/elements/progress-bars",
      name: "el-progress-bars",
      component: ElProgressBars,
    },
    {
      path: "/sections/elements/toggles",
      name: "el-toggles",
      component: ElToggles,
    },
    {
      path: "/sections/elements/typography",
      name: "el-typography",
      component: ElTypography,
    },
    // Not found handler
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: NotFoundPage,
    },
  ],
});
const pagesNeedAuth = [
  "profile",
  "document",
  "account",
  "tiptap-editor"
]
const loginPages = [
  "signin",
  "signup"
]
router.beforeEach((to, from) => {
  // Login guard
  console.log("to", to, "from", from)
  if (pagesNeedAuth.includes(to.name.toString())) {
    if (!getSessionUserDetail()) {
      return { name: "signin" }
    }
  }
  else if (loginPages.includes(to.name.toString())) {
    if (getSessionUserDetail()) {
      return { name: "profile" }
    }
  }

})

export default router;
