<script setup lang="ts">
import { reactive, onMounted, ref } from "vue";
import { UserDetail, getSessionUserDetail, emptyUserDetail } from "@/server/user";
import { requestFileList, uploadFile } from "@/server/file";
import { useUserStore } from "@/stores/user";
import { storeToRefs } from "pinia";
import { RouterLink } from "vue-router";
const userStore = useUserStore();
const userDetail = storeToRefs(userStore).userDetail;
const fileList = reactive<string[]>([])
const fileinput = ref<HTMLInputElement>(null)
function loadFileList() {
  if (userDetail.value.token) {

    requestFileList(userDetail.value.username, userDetail.value.token).then((res) => {
      console.log(res.data);
      fileList.splice(0, fileList.length, ...res.data.data);
    }).catch((err) => {
      console.log("请求文件列表失败", err);
    })
  }
}
onMounted(() => {
  loadFileList();
});
function handleUploadFile() {
  console.log("handleUploadFile", fileinput.value.files[0]);
  const file = fileinput.value.files[0];
  uploadFile(file, userDetail.value.username, userDetail.value.token).then((res) => {
    console.log(res);
    loadFileList();
  }).catch((err) => {
    console.log("上传文件失败", err);
  });
  fileinput.value.files = null;
  // axios.post("http://localhost:8080/upload", formData, {
  //   headers: {
  //     "Content-Type": "multipart/form-data",
  //   },
  // });
}
</script>
<template>
  <div class="row flex-row-reverse">
    <div class="col-3">
      <input type="file"
        accept="application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        class="w-0 h-0 invisible" ref="fileinput" @change="handleUploadFile">
      <button class="btn btn-success" @click="fileinput.click()">
        <i class="bi bi-file-earmark-plus"></i>
        <span>上传文件</span>
      </button>
    </div>
  </div>
  <div class="container w-100 d-flex flex-wrap">
    <div v-for="file in fileList">
      <div class="card m-2 border">
        <div class="card-body">
          <div class="card-title text-black">
            {{ file }}
          </div>

          <RouterLink :to="{ name: 'tiptap-editor', params: { filename: file } }"
            class="edit-route btn btn-success position-absolute bottom-0 end-0 mb-3 me-3">
            编辑<i class="bi bi-pencil-square"></i>
          </RouterLink>

        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  width: 16em;
  height: 12em;
}

.edit-route {
  width: 8em;
}
</style>