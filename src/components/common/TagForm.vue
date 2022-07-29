<template>
    <div style="text-align:left;width:30%;position:absolute;right:20px;top:20px;">
        <el-button v-show="show" type="primary" class='back-button' @click="backPage">提交标记<i
                class="el-icon-arrow-right"></i></el-button>
        <el-button v-show="!show" type="primary" class='back-button' @click="openPage">提交标记<i
                class="el-icon-arrow-left"></i></el-button>
        <el-card style="text-align:left;position:absolute;right:-600px;top:60px;height:590px;width:400px;"
            id="tagAddPage">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm"
                style="margin-top:0%;margin-left:-50px;margin-right:20px;" hide-required-asterisk="true">
                <el-form-item label="经度" prop="lng">
                    <el-input-number v-model="ruleForm.lng" size="small" controls-position="left" :precision="2"
                        :step="0.01" :min="-180" :max="180">
                    </el-input-number>
                </el-form-item>
                <el-form-item label="纬度" prop="lat">
                    <el-input-number v-model="ruleForm.lat" size="small" controls-position="left" :precision="2"
                        :step="0.01" :min="-90" :max="90">
                    </el-input-number>
                </el-form-item>
                <el-form-item label="标题" prop="title">
                    <el-input v-model="ruleForm.title" size="small"></el-input>
                </el-form-item>
                <el-form-item label="类型" prop="etype">
                    <el-select v-model="ruleForm.etype" placeholder="请选择类型" size="small">
                        <el-option label="动物" :value="2"></el-option>
                        <el-option label="植物" :value="3"></el-option>
                        <el-option label="景观" :value="4"></el-option>
                        <el-option label="矿物" :value="5"></el-option>
                        <el-option label="事件" :value="6"></el-option>
                        <el-option label="其他" :value="1"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="描述" prop="desc">
                    <el-input type="textarea" v-model="ruleForm.desc" maxlength="100" show-word-limit resize="none">
                    </el-input>
                </el-form-item>
                <el-form-item label="图片" prop="imgSrc">
                    <el-upload class="avatar-uploader" action="https://www.imgtp.com/api/upload" :show-file-list="false"
                        :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload" v-model="ruleForm.imgSrc">
                        <img v-if="ruleForm.imgSrc" :src="ruleForm.imgSrc" class="avatar">
                        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                </el-form-item>
                <el-form-item style="margin-top:0px;margin-left:40px;">
                    <el-button type="primary" @click="submitForm('ruleForm')">立即提交</el-button>
                    <el-button @click="resetForm('ruleForm')">重置</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>
<script>
import axios from 'axios';
import '../../common/dayjs.min.js'
import { mapState } from 'vuex'
export default {
    data() {
        return {
            show: false,
            image: undefined,
            userInfo: this.$store.state.data,
            ruleForm: {
                lng: undefined,
                lat: undefined,
                title: "",
                etype: "",
                desc: "",
                imgSrc: ""
            },
            rules: {
                lng: [
                    { required: true, message: "请输入标记所在经度，可通过定位获取", trigger: "blur" }
                ],
                lat: [
                    { required: true, message: "请输入标记所在纬度，可通过定位获取", trigger: "blur" }
                ],
                title: [
                    { required: true, message: "请输入标记名称", trigger: "blur" },
                    { min: 1, max: 10, message: "长度在 1 到 10 个字符", trigger: "blur" }
                ],
                etype: [
                    { required: true, message: "请选择标记类型", trigger: ['blur', 'change'] }
                ],
                desc: [
                    { required: true, message: "请填写100字以内的标记描述", trigger: "blur" }
                ],
                imgSrc: [
                    { required: true, message: "请上传标记展示图片", trigger: ["blur", 'change'] }
                ]
            }
        };
    },
    watch: {
        show() {
            this.userInfo = this.$store.state.data
        }
    },
    mounted() {
        this.$bus.$on('location', (data) => {
            this.ruleForm.lng = data.lng
            this.ruleForm.lat = data.lat
        })
    },
    beforeDestroy() {
        this.$bus.$off('location')
    },
    methods: {
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    let param = new FormData();
                    param.append('image', this.image);
                    axios.post('https://www.imgtp.com/api/upload', param)
                        .then(response=> {
                            this.ruleForm.imgSrc = response.data.data.url
                            let param2 = this.ruleForm
                            param2['type'] = this.userInfo.type
                            param2['uid'] = this.userInfo.uid
                            param2['time'] = dayjs(Date.now()).format('YYYY-MM-DD HH:mm:ss')
                            param2['imgSrc'] = response.data.data.url
                            console.log(param2,this.ruleForm)
                            return axios.post('http://localhost:8080/api/v1/upload', param2)
                        })
                        .then(response=> {
                            //that.image = undefined
                            this.resetForm(formName)
                            this.image = undefined
                            alert(response.data)
                            if(response.data==='不需审核，添加成功'){
                                location.reload()
                            }else{
                                this.backPage()
                            }
                            
                        })
                        .catch(error=> {
                            console.log(error);
                            alert('上传表单失败，请重试')
                        });
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        handleAvatarSuccess(_res, file) {
            this.image = file.raw;
            this.ruleForm.imgSrc = URL.createObjectURL(this.image);
        },
        beforeAvatarUpload(file) {
            const isJPG = file.type === 'image/jpeg';
            const isLt2M = file.size / 1024 / 1024 < 2;

            if (!isJPG) {
                this.$message.error('上传图片只能是 JPG 格式!');
            }
            if (!isLt2M) {
                this.$message.error('上传图片大小不能超过 2MB!');
            }
            return isJPG && isLt2M;
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        },
        backPage() {
            const page = document.getElementById("tagAddPage");
            page.style.right = "-600px";
            this.show = false
        },
        openPage() {
            const page = document.getElementById("tagAddPage");
            page.style.right = "40px";
            this.show = true
        }
    },
}
</script>
<style scoped>
.back-button {
    position: absolute;
    right: 40px;
}

.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.avatar-uploader .el-upload:hover {
    border-color: #409EFF;
}

.avatar-uploader-icon,
.avatar {
    font-size: 28px;
    color: #8c939d;
    width: 170px;
    height: 170px;
    line-height: 170px;
    text-align: center;
}
</style>