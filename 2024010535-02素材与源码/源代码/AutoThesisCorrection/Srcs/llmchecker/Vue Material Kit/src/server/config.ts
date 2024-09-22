import axios from "axios"

import { useUserStore } from "@/stores/user";
axios.interceptors.request.use(
    config => {
        const userStore = useUserStore()
        // 在发送请求之前做些什么
        if (userStore.isLogin) {
            const auth = userStore.userDetail.token ? "Bearer " + userStore.userDetail.token : ""
            console.log("Add token to request" + auth)
            config.headers.Authorization = auth
        }
        return config;
    }
);

export const TEST_PREFIX = "http://127.0.0.1:4523/m1/3148215-0-default"
// 后端地址
export const SERVER_PREFIX = "http://222.20.95.251:9999"
// export const SERVER_PREFIX = "http://127.0.0.1:9999"
// 用户信息接口
export const INFO_URL = "/users"
// 登录接口
export const LOGIN_URL = "/login"
// 注册接口
export const REGISTER_URL = "/register"
// 修改接口
export const UPDATE_URL = "/update/user"
// 删除接口
export const DELETE_URL = "/delete/user"
// 上传文件接口
export const UPLOAD_URL = "/upload"
// 获取文件列表接口
export const FILE_LIST_URL = "/list"
// 获取文件接口
export const FILE_URL = "/file"
// 更新文件接口
export const UPDATE_FILE_URL = "/update"