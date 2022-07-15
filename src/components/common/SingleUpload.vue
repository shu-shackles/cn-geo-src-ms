<!-- <template>
    <div class="upload-container">
        <el-upload :action="uploadUrl" name="avatar" :multiple="false" :show-file-list="false"
            :before-upload="beforeUpload" :on-success="handleUploadSuccess" :on-error="handleUploadError" :drag="drag"
            with-credentials :class="uploadClass">
            <div v-if="!drag">
                <el-button v-if="imageUrl" size="small" type="success">已上传，可点击修改</el-button>
                <el-button size="small" type="primary" v-else><i class="el-icon-upload el-icon--left"></i>点击上传
                </el-button>
            </div>
            <div v-if="drag">
                <i class="el-icon-upload" />
                <div class="el-upload__text">将单张图片（限jpg格式，大小不超过2M）拖到此处，或<em>点击上传</em></div>
            </div>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible" :append-to-body="true" :modal-append-to-body="false"
            :width="dialogWidth" class="preview-dialog">
            <img width="100%" :src="imageUrl" alt="" />
        </el-dialog>
        <div v-if="!drag && imageUrl.length > 0" class="el-upload-list el-upload-list--text">
            <div class="el-upload-list__item is-success">
                <a class="el-upload-list__item-name" @click="handlePreview"> <i class="el-icon-picture"></i>点此处预览</a>
                <label class="el-upload-list__item-status-label">
                    <i class="el-icon-upload-success el-icon-circle-check"></i>
                </label>
                <i class="el-icon-close" @click="removeImage"></i>
            </div>
        </div>
        <div v-if="drag && imageUrl.length > 0" class="el-upload-list el-upload-list--picture-card">
            <div class="el-upload-list__item is-success">
                <img :src="imageUrl" alt="" class="el-upload-list__item-thumbnail" />
                <label class="el-upload-list__item-status-label">
                    <i class="el-icon-upload-success el-icon-check"></i>
                </label>
                <i class="el-icon-close"></i>
                <i class="el-icon-close-tip">按 delete 键可删除</i>
                <span class="el-upload-list__item-actions">
                    <span class="el-upload-list__item-preview">
                        <i class="el-icon-zoom-in" @click="handlePreview"></i>
                    </span>
                    <span class="el-upload-list__item-delete">
                        <i class="el-icon-delete" @click="removeImage"></i>
                    </span>
                </span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SingleUpload',
    props: {
        value: {
            type: String,
            default: ''
        },
        drag: {
            type: Boolean,
            default: false
        },
        dialogWidth: {
            type: String,
            default: '35%'
        }
    },
    data() {
        return {
            dialogVisible: false
        }
    },
    computed: {
        uploadUrl() {
            const url = process.env.VUE_APP_BASE_API + '/admin/single/upload'
            return url
        },
        imageUrl() {
            return this.value ? process.env.VUE_APP_BASE_API + this.value : ''
        },
        uploadClass() {
            return this.drag ? 'image-uploader' : ''
        }
    },
    methods: {
        removeImage() {
            this.$confirm(`确定移除已上传的图片？`, '提示').then(() => {
                this.emitInput('')
            })
        },
        emitInput(val) {
            this.$emit('input', val)
        },
        handleUploadSuccess(response) {
            this.emitInput(this.commonApi.uploadSuccess(response))
        },
        handleUploadError(err) {
            this.$message.error(err.message)
        },
        handleUploadRemove() {
            this.emitInput('')
        },
        beforeUpload(file) {
            const typeList = ['image/jpeg', 'image/png', 'image/gif']
            const isTypeValid = typeList.includes(file.type)
            const isLt2M = file.size / 1024 / 1024 < 2
            if (!isTypeValid) {
                this.$message.error('图片格式只能是 JPG/PNG/GIF!')
            }
            if (!isLt2M) {
                this.$message.error('图片大小不能超过 2MB!')
            }
            return isTypeValid && isLt2M
        },
        handlePreview() {
            this.dialogVisible = true
        }
    }
}
</script>

<style lang="scss" scoped>
.upload-container {
    width: 100%;
    position: relative;
    display: flex;
    flex-direction: row;

    .image-uploader {
        width: 150px;
        margin-right: 20px;

        .el-icon-upload {
            margin: 20px 0 16px;
            font-size: 60px;
        }

        .el-upload__text {
            line-height: 20px;
            font-size: 13px;
        }
    }

    .el-upload-list--text {
        margin: 6px 0 0 10px;
    }

    .image-uploader /deep/ .el-upload-dragger {
        width: 150px;
        height: 150px;
    }

    .el-upload__tip {
        margin: 0 0 0 15px;
    }

    .el-upload-list__item:first-child {
        margin: 0;
    }
}

.preview-dialog /deep/ .el-dialog__header {
    padding: 0;
}

.preview-dialog /deep/ .el-dialog__body {
    padding: 20px;
}
</style> -->

<template>
  <div class="component-upload-image">
    <el-upload :v-show="fileList.length===0?true:false" :disabled="disabled"
      :action="uploadImgUrl"
      list-type="picture-card"
      :http-request="uploadRequest"
      :on-success="handleUploadSuccess"
      :before-upload="handleBeforeUpload"
      :limit="limit"
      :on-error="handleUploadError"
      :on-exceed="handleExceed"
      name="file"
      :multiple="multiple"
      :on-remove="handleRemove"
      :show-file-list="true"
      :headers="headers"
      :file-list="fileList"
      :on-preview="handlePictureCardPreview"
      :class="{hide: this.fileList.length >= this.limit}"
    >
      <i class="el-icon-plus"></i>
    </el-upload>

    <!-- 上传提示 -->
    <div class="el-upload__tip" slot="tip" v-if="showTip">
      请上传
      <template v-if="fileSize"> 大小不超过 <b style="color: #f56c6c">{{ fileSize }}MB</b> </template>
      <template v-if="fileType"> 格式为 <b style="color: #f56c6c">{{ fileType.join("/") }}</b> </template>
      的文件
    </div>

    <el-dialog
      :visible.sync="dialogVisible"
      title="预览"
      width="800"
      append-to-body
    >
      <img
        :src="dialogImageUrl"
        style="display: block; max-width: 100%; margin: 0 auto"
      />
    </el-dialog>
  </div>
</template>

<script>
//import { getToken } from "@/utils/auth";
import axios from 'axios';
export default {
  props: {
    value: [String, Object, Array],
    // 图片数量限制
    limit: {
      type: Number,
      default: 1,
    },
    // 大小限制(MB)
    fileSize: {
       type: Number,
      default: 2,
    },
    // 文件类型, 例如['png', 'jpg', 'jpeg']
    fileType: {
      type: Array,
      default: () => [ "jpg" ],
    },
    // 是否显示提示
    isShowTip: {
      type: Boolean,
      default: true
    },
    disabled: {
      type: Boolean,
      default: false
    },
    multiple: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      dialogImageUrl: "",
      dialogVisible: false,
      hideUpload: false,
      uploadImgUrl: process.env.VUE_APP_BASE_API + "/file/upload", // 上传的图片服务器地址
      headers: {
        Authorization: "Bearer " + getToken(),
      },
      fileList: []
    };
  },
  watch: {
    value: {
      handler(val) {
        if (val) {
          // 首先将值转为数组
          const list = Array.isArray(val) ? val : this.value.split(',');
          // 然后将数组转为对象数组
          this.fileList = list.map(item => {
            if (typeof item === "string") {
              item = { name: item, url: item };
            }
            return item;
          });
        } else {
          this.fileList = [];
          return [];
        }
      },
      deep: true,
      immediate: true
    }
  },
  computed: {
    // 是否显示提示
    showTip() {
      return this.isShowTip && (this.fileType || this.fileSize);
    },
  },
  methods: {
    // 上传多图片
    uploadRequest(param){
      let fileObj = param.file;
        let form = new FormData();
        form.append('file', fileObj);
        axios.post(this.uploadImgUrl, form, {
          headers:this.headers,
          process: function (event) {
            param.file.percent = event.loaded / event.total * 100;
            param.onprogress(param.file);
          }
        }).then(res => {
          this.handleUploadSuccess(res.data);
        }).catch(res => {
          this.handleUploadError();
        });
    },
    // 删除图片
    handleRemove(file, fileList) {
      const findex = this.fileList.map(f => f.name).indexOf(file.name);
      this.fileList.splice(findex, 1);
      this.$emit("input", this.listToString(this.fileList));
    },
    // 上传成功回调
    handleUploadSuccess(res) {
      console.log(res);
      this.fileList.push({ name: res.data.url, url: res.data.url });
      this.$emit("input", this.listToString(this.fileList));
      this.loading.close();
    },
    // 上传前loading加载
    handleBeforeUpload(file) {
      let isImg = false;
      if (this.fileType.length) {
        let fileExtension = "";
        if (file.name.lastIndexOf(".") > -1) {
          fileExtension = file.name.slice(file.name.lastIndexOf(".") + 1);
        }
        isImg = this.fileType.some(type => {
          if (file.type.indexOf(type) > -1) return true;
          if (fileExtension && fileExtension.indexOf(type) > -1) return true;
          return false;
        });
      } else {
        isImg = file.type.indexOf("image") > -1;
      }
      if (!isImg) {
        this.$message.error(
          `文件格式不正确, 请上传${this.fileType.join("/")}图片格式文件!`
        );
        return false;
      }
      if (this.fileSize) {
        const isLt = file.size / 1024 / 1024 < this.fileSize;
        if (!isLt) {
          this.$message.error(`上传头像图片大小不能超过 ${this.fileSize} MB!`);
          return false;
        }
      }
      this.loading = this.$loading({
        lock: true,
        text: "上传中",
        background: "rgba(0, 0, 0, 0.7)",
      });
    },
    // 文件个数超出
    handleExceed() {
      this.$message.error(`上传文件数量不能超过 ${this.limit} 个!`);
    },
    // 上传失败
    handleUploadError() {
      this.$message({
        type: "error",
        message: "上传失败",
      });
      this.loading.close();
    },
    // 预览
    handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
    },
    // 对象转成指定字符串分隔
    listToString(list, separator) {
      let strs = "";
      separator = separator || ",";
      for (let i in list) {
        strs += list[i].url + separator;
      }
      return strs != '' ? strs.substr(0, strs.length - 1) : '';
    }
  }
};
</script>
<style scoped lang="scss">
// .el-upload--picture-card 控制加号部分
::v-deep.hide .el-upload--picture-card {
    display: none;
}
// 去掉动画效果
::v-deep .el-list-enter-active,
::v-deep .el-list-leave-active {
    transition: all 0s;
}
::v-deep .el-list-enter, .el-list-leave-active {
    opacity: 0;
    transform: translateY(0);
}
</style>