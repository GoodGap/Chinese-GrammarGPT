<script setup>
import RotatingCard from "../../../examples/cards/rotatingCards/RotatingCard.vue";
import RotatingCardFront from "../../../examples/cards/rotatingCards/RotatingCardFront.vue";
import RotatingCardBack from "../../../examples/cards/rotatingCards/RotatingCardBack.vue";
import DefaultInfoCard from "../../../examples/cards/infoCards/DefaultInfoCard.vue";
</script>
<template>
  <section class="my-5 py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-4 ms-auto me-auto p-lg-4 mt-lg-0 mt-4">
          <RotatingCard>
            <RotatingCardFront
              image="https://images.unsplash.com/photo-1569683795645-b62e50fbf103?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80"
              class="w-100" icon="touch_app" title="智能纠错系统" description="您可以使用此系统来协助您进行论文撰写与纠错" />

            <RotatingCardBack
              image="https://images.unsplash.com/photo-1498889444388-e67ea62c464b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1365&q=80"
              title="性能领先" description="准确率更高且更加高效的纠错系统" :action="[
                {
                  route: { name: 'signin' },
                  label: '开始体验',
                },
              ]" />
          </RotatingCard>
        </div>
        <div class="col-lg-6 ms-auto">
          <div class="row justify-content-start">
            <DefaultInfoCard icon="content_copy" title="用户体验出色"
              description="注册流程简单，用户信息加密保存于后端数据库，前后端与模型端实时配合给出纠错反馈，帮助科研人员高效完成论文纠错改错任务。" />
            <DefaultInfoCard icon="flip_to_front" title="文本格式多样"
              description="系统可以接受docx、html、txt等多种类型文本，可满足不同种类的用户需求。系统还支持在网页端进行文本的修改与格式的调整，并支持一键导出下载功能" />
          </div>
          <div class="row justify-content-start mt-5">
            <DefaultInfoCard class="mt-3" icon="price_change" title="模型性能强大"
              description="使用大语言模型ChatGLM-6B作为基准模型，在保证处理速度的基础上，具有理解上下文的能力，且可以随用户使用不断学习文本特征，提高准确性与合理性。" />
            <DefaultInfoCard class="mt-3" icon="devices" title="纠错类型全面"
              description="项目已人工标注了高质量数据集，能识别并改正绝大多数主要病句类型，包括搭配不当、结构混乱、语序不当、不合逻辑、成分残缺、成分冗余等。" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
