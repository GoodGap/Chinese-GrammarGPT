<script setup>
import DefaultCounterCard from "../../../examples/cards/counterCards/DefaultCounterCard.vue";
</script>

<template>
  <section class="pt-3 pb-4" id="count-stats">
    <div class="container">
      <div class="row">
        <div class="col-lg-9 z-index-2 border-radius-xl mx-auto py-3">
          <div class="row">
            <div class="col-md-4 position-relative">
              <DefaultCounterCard color="success" title="拼写错误" description="" suffix="✔️" :duration="3000"
                divider="vertical" :require-count="false" />
            </div>
            <div class="col-md-4 position-relative">
              <DefaultCounterCard color="success" title="语法错误" description="" :count="6" suffix="种" :duration="3000"
                divider="vertical" />
            </div>
            <div class="col-md-4">
              <DefaultCounterCard color="success" title="逻辑错误" description="" suffix="✔️" :duration="3000"
                :require-count="false" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
