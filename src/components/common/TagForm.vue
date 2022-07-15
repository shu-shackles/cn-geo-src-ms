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
                <el-form-item label="经度" prop="x">
                    <el-input-number v-model="ruleForm.x" size="small" controls-position="left" :precision="2"
                        :step="0.01" :min="-180" :max="180">
                    </el-input-number>
                </el-form-item>
                <el-form-item label="纬度" prop="y">
                    <el-input-number v-model="ruleForm.y" size="small" controls-position="left" :precision="2"
                        :step="0.01" :min="-90" :max="90">
                    </el-input-number>
                </el-form-item>
                <el-form-item label="标题" prop="name">
                    <el-input v-model="ruleForm.name" size="small"></el-input>
                </el-form-item>
                <el-form-item label="类型" prop="type">
                    <el-select v-model="ruleForm.type" placeholder="请选择类型" size="small">
                        <el-option label="动物" value="动物"></el-option>
                        <el-option label="植物" value="植物"></el-option>
                        <el-option label="景观" value="景观"></el-option>
                        <el-option label="矿物" value="矿物"></el-option>
                        <el-option label="事件" value="事件"></el-option>
                        <el-option label="其他" value="其他"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="描述" prop="desc">
                    <el-input type="textarea" v-model="ruleForm.desc" maxlength="100" show-word-limit resize="none">
                    </el-input>
                </el-form-item>
                <el-form-item label="图片" prop="image">
                    <!-- <SingleUpload v-model='ruleForm.imgSrc' :dialogWidth="0.3" drag /> -->
                    <ele-upload-image action="http://localhost:8080/api/v1/upload_image" v-model="image"
                        :responseFn="handleResponse"></ele-upload-image>
                </el-form-item>
                <el-form-item style="margin-top:0px;">
                    <el-button type="primary" @click="submitForm('ruleForm')">立即提交</el-button>
                    <el-button @click="resetForm('ruleForm')">重置</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>
<script>
import SingleUpload from './SingleUpload.vue';
import EleUploadImage from "vue-ele-upload-image";
export default {
    data() {
        return {
            show: false,
            ruleForm: {
                //position: {
                x: undefined,
                y: undefined,
                //},
                name: "",
                type: "",
                desc: "",
                image: undefined,
                imgSrc: ""
            },
            rules: {
                x: [
                    { required: true, message: "请输入标记所在经度，可通过定位获取", trigger: "blur" }
                ],
                y: [
                    { required: true, message: "请输入标记所在纬度，可通过定位获取", trigger: "change" }
                ],
                name: [
                    { required: true, message: "请输入标记名称", trigger: "blur" },
                    { min: 1, max: 10, message: "长度在 1 到 10 个字符", trigger: "blur" }
                ],
                type: [
                    { required: true, message: "请选择标记类型", trigger: "select" }
                ],
                desc: [
                    { required: true, message: "请填写100字以内的标记描述", trigger: "blur" }
                ],
                image: [
                    { required: true, message: "请上传标记展示图片", trigger: "blur" }
                ]
            }
        };
    },
    methods: {
        handleResponse(response, file, fileList) {
            // 根据响应结果, 设置 URL
            this.imgSrc = response.data[0]
            this.image = require('@/assets/images/ico2.png')
        },
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    alert("submit!");
                }
                else {
                    console.log("error submit!!");
                    return false;
                }
            });
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
    components: { SingleUpload, EleUploadImage }
}
</script>
<style scoped>
.back-button {
    position: absolute;
    right: 40px;
}

.el-textarea__inner {
    resize: none;
}
</style>