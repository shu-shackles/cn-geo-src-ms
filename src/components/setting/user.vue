<template>
<div class="survey_content2 clearfix">
  <el-button class='right' type="success" size="small" @click='add'>添加用户</el-button>
  <div class="contents clearfix">    
    <el-table :data="userData" style="width: 100%" :default-sort = "{prop: 'uid', order: 'ascending'}" >
    <el-table-column prop="uid" label="UID" sortable width="80"></el-table-column>
    <el-table-column prop="name" label="用户名称"></el-table-column>
    <el-table-column prop="password" label="用户密码"></el-table-column>
    <el-table-column prop="type" label="用户类型"></el-table-column>
    <el-table-column prop="area" label="地区"></el-table-column>
    <el-table-column prop="IDName" label="姓名"></el-table-column>
    <el-table-column prop="ID" label="身份证号"></el-table-column>
    <!-- <el-table-column prop="add" label="创建时间" sortable></el-table-column>
    <el-table-column prop="change" label="修改时间" sortable></el-table-column> -->
    <el-table-column label="操作" width="150">
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除
        </el-button>
        <el-button
          size="mini"
          type="warning"
          @click="clickEdit(scope.$index, scope.row)">编辑
        </el-button>
        <el-dialog title="编辑用户信息" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="用户密码" :label-width="formLabelWidth">
            <el-input v-model="form.password" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="用户类型" :label-width="formLabelWidth">
            <el-select v-model="form.type" placeholder="请选择用户类型">
              <el-option label="管理员" value="0"></el-option>
              <el-option label="地质勘探员" value="1"></el-option>
              <el-option label="普通用户" value="2"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="用户区域" :label-width="formLabelWidth">
            <el-input v-model="form.area" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
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
  export default {
    data() {
      return {
      userData:[],
      dialogFormVisible: false,
      form: {
        uid:'',
        name: '',
        password: '',
        type: '',
        area: '',
        IDName: '',
        ID: ''
      },
      formLabelWidth: '120px'      
      }
    },
    mounted(){
      this.QueryUser();
    },
    methods: {
      //查询所有用户
      QueryUser() {
        this.axios.post('allusers')
          .then(res => {
            if (res.status === 200) {
              console.log(res);
              this.userData=res.data;
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
  margin: 60px 20px;
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

