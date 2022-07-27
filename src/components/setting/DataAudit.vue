<template>
<div class="survey_content2 clearfix">
  <!-- <p>当前用户的token为：{{data}}</p> -->
  <!-- <el-button class='right' type="success" size="small" @click='add'>添加用户</el-button> -->
  <div class="contents clearfix">    
    <el-table :data="tagData" style="width: 100%" :default-sort = "{prop: 'eid', order: 'ascending'}" >
    <el-table-column prop="uid" label="UID" sortable width="80"></el-table-column>
    <el-table-column prop="eid" label="标记ID"></el-table-column>
    <!-- <el-table-column prop="password" label="用户密码"></el-table-column> -->
    <el-table-column prop="time" label="提交时间"></el-table-column>
    <el-table-column prop="title" label="标题"></el-table-column>
    <el-table-column prop="tag_sesc" label="描述"></el-table-column>
    <!-- <el-table-column prop="ID" label="身份证号"></el-table-column> -->
    <!-- <el-table-column prop="add" label="创建时间" sortable></el-table-column>
    <el-table-column prop="change" label="修改时间" sortable></el-table-column> -->
    <el-table-column label="操作" width="150">
      <template slot-scope="scope">

        <el-button
          size="mini"
          type="warning"
          @click="clickEdit(scope.$index, scope.row)">审核
        </el-button>
        <el-dialog title="审核标记信息" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <!-- <el-form-item label="用户密码" :label-width="formLabelWidth">
            <el-input v-model="form.password" autocomplete="off"></el-input>
          </el-form-item> -->
          <el-form-item label="标记类型" :label-width="formLabelWidth">
            <el-select v-model="form.type" readonly placeholder="请审核标记类型">
                <el-option label="动物" :value="2"></el-option>
                <el-option label="植物" :value="3"></el-option>
                <el-option label="景观" :value="4"></el-option>
                <el-option label="矿物" :value="5"></el-option>
                <el-option label="事件" :value="6"></el-option>
                <el-option label="其他" :value="1"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item readonly label="用户区域" :label-width="formLabelWidth">
            <el-input v-model="form.area" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="handleEdit">确 定</el-button>
        </div>
      </el-dialog>
        <!-- <el-button
          size="mini"
          type="primary"
          @click="handleEdit(scope.$index, scope.row)">分配
        </el-button> -->
      </template>
    </el-table-column>
  </el-table>
  </div>

</div>
  
</template>

<script>
  import { mapState } from 'vuex'; 
  export default {
    data() {
      return {
      readonly: true,
      tagData:[],
      dialogFormVisible: false,
      form: {
        uid:'',
        eid: '',
        title: '',
        tag_sesc: '',
        area: '',
        lng: '',
        lat: '',
        enentype:'',
        time:'',
        imgSrc:''
      },
      formLabelWidth: '120px'      
      }
    },
    computed:{
      ...mapState(['data'])
    },
    mounted(){
      this.QueryTag();
    },
    methods: {
      //查询所有标记
      QueryTag() {
        this.axios.post('areainformaltags'+"/全部")
          .then(res => {
            if (res.status === 200) {
              console.log(res);
              this.tagData=res.data;
            }else{
              //如果登录失败，重置表单，重新填写
              //element的消息提示组件
              console.log(res)
            }
          })
          .catch(err => {
            console.log(2)
            console.log(err)
          })
      },
      //点击编辑按钮
      clickEdit(index, row) {
        this.form.uid=row.uid;
        this.form.type=row.type;
        this.form.password=row.password;
        this.form.area=row.area;
        this.dialogFormVisible = true;
        console.log(index, row);
        var rowValue = row;
        console.log(rowValue);
      },
      //编辑信息
      handleEdit(){
        if(this.form.uid===1){
          this.$message({
          message: '超级管理员不可以编辑',
          type: 'error'
          });
          return
        }
        this.dialogFormVisible = false;
        this.axios.post('setinfo_type_area', {
            uid: this.form.uid,
            type: this.form.type,
            area:this.form.area
        })
        .then(res => {
            if (res.status === 200) {
              console.log(res);
              this.$message.success('修改成功！');
              this.QueryUser();
              // this.userData.splice(index,1)
            }else{
              //element的消息提示组件
              console.log(res);
              this.$message.error('修改失败: '+res.data+' 请重试！');
            } 
        })
        .catch(err => {
            console.log(4);
            console.log(err);
          })
      },
      // 删除
      handleDelete(index, row) {
        this.form.uid=row.uid;
        console.log(index, row);
        if(row.uid===1){
          this.$message({
          message: '超级管理员不可以删除',
          type: 'error'
          });
          return
        }
        this.axios.delete('deleteuser', {
          data: {
            uid: row.uid
          }
        })
        .then(res => {
            if (res.status === 200) {
              console.log(res);
              this.userData.splice(index,1)
            }else{
              //如果删除失败，重置表单，重新填写
              //element的消息提示组件
              console.log(res)
              this.$message.error('删除失败: '+res.data+' 请重试！')
            } 
        })
        .catch(err => {
            console.log(4)
            console.log(err)
          })

      },
      // 创建角色
      add(){
        this.dialogFormVisible=true
      }
    }
  }
</script>
<style lang="less" scoped>
@import '../../../static/css/clear';
@import '../../../static/css/common';
.survey_content2{
   width: 99.5%;
  // height: 100%;
  .body{
    height: 100%;
  }
  .contents{
  background-color: #fff;
  // background-color: rgb(198, 219, 212);
  margin: 0px 0px 60px 20px;
  padding: 15px;
  height: 100%;
  }
  .right{
    // height: 30px;
    position: absolute;
    right: 20px;
    top: 20px;
  }

}
</style>

