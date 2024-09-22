import axios, { Axios, AxiosResponse } from "axios";
import { SERVER_PREFIX, INFO_URL, UPDATE_URL, DELETE_URL, LOGIN_URL, REGISTER_URL } from './config'

export interface User {
    username: string,
    password: string,
    id?: number,
    token?: string,
    [key: string]: any
}
export function emptyUser(): User {
    return {
        username: "",
        password: ""
    }
}

export interface UserDetail {
    username: string,
    password: string,
    telephone: string,
    email: string,
    address: string,
    id?: number,
    token?: string,
    [key: string]: any
}

export function emptyUserDetail(): UserDetail {
    return {
        username: "",
        password: "",
        telephone: "",
        email: "",
        address: ""
    }
}

export function getTestUserDetail(): UserDetail {
    return {
        username: "testusername",
        password: "testpassword",
        telephone: "123456789",
        address: "test address",
        email: "testemail@mail.com",
    }
}

export interface LoginInfo {
    id: number,
    login_time: string,
    token: string,
    username: string
}

export interface ServerResponse {
    code: number,
    msg: string,
    data?: UserDetail,
    login_info?: LoginInfo
}

/**
 * 获取用户信息
 * @param username 用户名称，为空则获取所有用户信息
 */
export function getUserDetail(username?: string) {
    let url = SERVER_PREFIX + INFO_URL + (username ? "/" + username : "")
    return axios.get(url)
}

/**
 * 更新用户
 * @param userDetail 用户信息
 */
export function userUpdate(userDetail: UserDetail) {
    console.log(userDetail)
    userDetail.admin_user = userDetail.username
    return axios.put(
        SERVER_PREFIX + UPDATE_URL + `/${userDetail.id}`,
        userDetail
    )
}

/**
 * 用户登录
 * @param user 用户账密信息
 * @returns 请求结果，code: 0登录成功
 */
export function userSignIn(user: User): Promise<AxiosResponse<any, any>> {
    console.log("login")
    console.log(user)
    return axios.post(
        SERVER_PREFIX + LOGIN_URL,
        user
    )
}


/**
 * 用户注册
 * @param userDetail 用户详细信息
 * @returns 请求结果
 */
export function userSignUp(userDetail: UserDetail) {
    console.log("register")
    console.log(userDetail)
    return axios.post(
        SERVER_PREFIX + REGISTER_URL,
        userDetail
    )
}

export function deleteUser(userDetail: UserDetail) {
    userDetail.admin_user = userDetail.username
    console.log("delete" + userDetail)
    return axios.post(
        SERVER_PREFIX + DELETE_URL + "/" + userDetail.username,
        userDetail
    )
}

export function setSessionUserDetail(userDetail: UserDetail) {
    userDetail.password = ""
    sessionStorage.setItem("userDetail", JSON.stringify(userDetail))
}

export function getSessionUserDetail(): UserDetail | null {
    let userDetail = sessionStorage.getItem("userDetail")
    if (userDetail && userDetail.length > 0) {
        return JSON.parse(userDetail)
    }
    return null
}