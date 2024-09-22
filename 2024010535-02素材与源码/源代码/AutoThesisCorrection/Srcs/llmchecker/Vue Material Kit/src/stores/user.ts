import { defineStore } from "pinia";
import { UserDetail, emptyUserDetail, setSessionUserDetail, getSessionUserDetail } from "@/server/user";
import { ref, computed } from "vue";
export const useUserStore = defineStore("userDetail", () => {
    const mUserDetail = ref<UserDetail>(getSessionUserDetail() ?? emptyUserDetail());
    const userDetail = computed<UserDetail>({
        get() {
            return mUserDetail.value;
        },
        set(newUserDetail: UserDetail) {
            console.log("set userDetail")
            setSessionUserDetail(newUserDetail);
            mUserDetail.value = newUserDetail
        }
    })
    const isLogin = computed<boolean>(() => {
        return userDetail.value.token !== undefined && userDetail.value.token.length > 0
    })
    return {
        userDetail,
        isLogin,
    };
});
