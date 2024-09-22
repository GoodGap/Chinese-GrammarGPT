/*
=========================================================
* Vue Material Kit 2 - v1.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/vue-material-kit-pro
* Copyright 2021 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

const imagesPrefix =
  "https://raw.githubusercontent.com/creativetimofficial/public-assets/master/material-design-system/presentation/sections";

import imgBold from "@/assets/img/examples/example_bold.jpg"
import imgItalic from "@/assets/img/examples/example_italic.jpg"
import imgDelete from "@/assets/img/examples/example_delete.jpg"
import imgUList from "@/assets/img/examples/example_ulist.jpg"
import imgOList from "@/assets/img/examples/example_olist.jpg"
import imgTable from "@/assets/img/examples/example_table.jpg"
import imgHeader from "@/assets/img/examples/example_header.jpg"
import imgError1 from "@/assets/img/examples/example_error_1.jpg"
import imgError2 from "@/assets/img/examples/example_error_2_结构混乱.jpg"
import imgError3 from "@/assets/img/examples/example_error_3语序不当.jpg"
import imgError4 from "@/assets/img/examples/example_error_4_不合逻辑.jpg"
import imgError5 from "@/assets/img/examples/example_error_5_成分残缺.jpg"
import imgError6 from "@/assets/img/examples/example_error_6_成分冗余.jpg"
export default [
  {
    heading: "文本编辑",
    description:
      "提供多种样式修改。支持导入和导出多种文档格式",
    items: [
      {
        image: imgBold,
        title: "加粗",
        pro: false
      },
      {
        image: imgItalic,
        title: "斜体",
        pro: false
      },
      {
        image: imgDelete,
        title: "删除线",
        pro: false
      },
      {
        image: imgUList,
        title: "无序列表",
        pro: false
      },
      {
        image: imgOList,
        title: "有序列表",
        pro: false
      },
      {
        image: imgTable,
        title: "表格",
        pro: false
      },
      {
        image: imgHeader,
        title: "多级标题",
        pro: false
      },
    ]
  },
  {
    heading: "错误纠正",
    description: "提供错误的详细描述以及纠正方法  ",
    items: [
      {
        image: imgError1,
        title: "搭配不当",
        pro: false
      },
      {
        image: imgError2,
        title: "结构混乱",
        subtitle: "2 Nav Tabs",
        route: "navigation-navtabs",
        pro: false
      },
      {
        image: imgError3,
        title: "语序不当",
        pro: false
      },
      {
        image: imgError4,
        title: "不合逻辑",
        pro: false
      },
      {
        image: imgError5,
        title: "成分残缺",
        pro: false
      },
      {
        image: imgError6,
        title: "成分冗余",
        pro: false
      }
    ]
  },
];
