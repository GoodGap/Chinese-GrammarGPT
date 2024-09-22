import axios, { AxiosResponse } from "axios";
import { SERVER_PREFIX, UPLOAD_URL, FILE_LIST_URL, FILE_URL, UPDATE_FILE_URL } from "./config";
interface FileListResponse {
    code: number,
    msg: string,
    data?: string[]
}
export function uploadFile(file: File, username: string, token: string) {
    const formData = new FormData()
    formData.append('files', file)
    formData.append('username', username)
    formData.append('token', token)
    return axios.post(SERVER_PREFIX + UPLOAD_URL, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then(response => {
        console.log('上传成功', response.data);
    }).catch(error => {
        console.error('上传失败', error);
    });
}

export function requestFileList(username, token): Promise<AxiosResponse<FileListResponse>> {
    return axios.post(SERVER_PREFIX + FILE_LIST_URL + `/${username}`, {
        "token": token
    })
}

export function requestFile(username: string, filename: string) {
    return axios.get(SERVER_PREFIX + FILE_URL + `/${username}/${filename}`, {
        responseType: 'blob',
        timeout: 10000,
    })
}



export function updateFile(html: string, username: string, filename: string, token: string) {
    return axios.post(SERVER_PREFIX + UPDATE_FILE_URL + `/${username}/${filename}`,
        {
            "token": token,
            "content": html
        }
    )
}

