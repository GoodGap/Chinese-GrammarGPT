<script setup lang="ts">
import { onMounted } from "vue";

// Sections components
import BaseLayout from "@/layouts/sections/components/BaseLayout.vue";

</script>
<template>
  <BaseLayout title="成员介绍" :breadcrumb="[{ label: '文档', route: '#' }, { label: '成员介绍' }]">
    <div class="border-radius-xl overflow-hidden shadow-lg mb-7 p-4">
      <!-- table title -->
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h6 class="mb-0">成员介绍</h6>
      </div>
      <div class="table-responsive">
        <table class="table table-striped table-bordered">
          <thead>
            <tr>
              <th>成员姓名</th>
              <th>学号</th>
              <th>年级</th>
              <th>QQ</th>
              <th>院系/专业</th>
              <th>联系电话</th>
              <th>项目分工</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>李嘉鹏</td>
              <td>U202115652</td>
              <td>大二</td>
              <td>1633741074</td>
              <td>数据科学与大数据技术</td>
              <td>18986139698</td>
              <td>策划、查阅文献、撰写材料、统筹项目整体进度</td>
            </tr>
            <tr>
              <td>崔昊阳</td>
              <td>U202115415</td>
              <td>大二</td>
              <td>915309346</td>
              <td>计算机科学与技术</td>
              <td>13803378320</td>
              <td>对现有大语言模型进行微调、智能纠错系统模型搭建和植入</td>
            </tr>
            <tr>
              <td>高朗</td>
              <td>U202115641</td>
              <td>大二</td>
              <td>2504118719</td>
              <td>计算机科学与技术</td>
              <td>15169152356</td>
              <td>构造高质量学术论文错误数据集、对项目优化后的模型进行微调</td>
            </tr>
            <tr>
              <td>裴俊博</td>
              <td>U202115630</td>
              <td>大二</td>
              <td>391745259</td>
              <td>计算机科学与技术</td>
              <td>15735971197</td>
              <td>搭建系统客户端的在线交互页面</td>
            </tr>
            <tr>
              <td>王颖彬</td>
              <td>U202115647</td>
              <td>大二</td>
              <td>1548271672</td>
              <td>计算机科学与技术</td>
              <td>15172576219</td>
              <td>查阅文献、撰写成果总结材料等</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h6 class="mb-0">指导教师介绍</h6>
      </div>
      <div class="table-responsive">
        <table class="table table-striped table-bordered">
          <tbody>
            <tr>
              <td>姓名：</td>
              <td colspan="3">李瑞轩</td>
              <td>工作单位：</td>
              <td colspan="2">华中科技大学计算机科学与技术学院</td>
              <td></td>
            </tr>
            <tr>
              <td>职称:</td>
              <td>教授</td>
              <td>职务：</td>
              <td>教师</td>
              <td>E-mail: </td>
              <td colspan="2">rxli@hust.edu.cn</td>
              <td></td>
            </tr>
            <tr class="odd">
              <td>研究方向：</td>
              <td colspan="3">分布式计算与云计算</td>
              <td>联系电话：</td>
              <td colspan="2">027-87544285</td>
              <td></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </BaseLayout>
</template>