<template>
<div class="survey_content2 clearfix">
  <!-- <p>当前用户的token为：{{data}}</p> -->
  <!-- <el-button class='right' type="success" size="small" @click='add'>添加用户</el-button> -->
  <div class="contents clearfix">
    <el-row type="flex" justify="left">
      <el-input style="width:250px ;margin: 5px 5px 5px 5px;"
        placeholder="请输入用户名"
        prefix-icon="el-icon-search"
        v-model="inputName"
        clearable>
      </el-input>
      <el-button type="primary" icon="el-icon-search" @click="QueryInfo(inputName)" style=" margin: 5px 5px 5px 5px;" circle></el-button>
    </el-row>  
    <el-table :data="userData.slice(
        (pageInfo.currentPage - 1) * pageInfo.pageSize,
        pageInfo.currentPage * pageInfo.pageSize
      )"  :header-cell-style="{background:'#eee',color:black}" style="width: 100%" :default-sort = "{prop: 'uid', order: 'ascending'} "  >
    <el-table-column  prop="uid" label="UID" align="center" sortable width="180"></el-table-column>
    <el-table-column  prop="name" label="用户名称" align="center"  width="120">

    </el-table-column>
    <!-- <el-table-column prop="password" label="用户密码"></el-table-column> -->
    <el-table-column prop="type" label="用户类型" align="center" :formatter="typeFormat"></el-table-column>
    <el-table-column prop="area" :formatter="areaFormat" label="地区" align="center"   width="150">
    </el-table-column>
    <el-table-column prop="IDName" label="姓名" align="center" width="150">

    </el-table-column>
    <el-table-column prop="ID" align="center" label="身份证号"></el-table-column>
    <!-- <el-table-column prop="add" label="创建时间" sortable></el-table-column>
    <el-table-column prop="change" label="修改时间" sortable></el-table-column> -->
    <el-table-column label="操作" header-align="center" width="200">
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="danger"
          icon="el-icon-delete"
          @click="handleDelete(scope.$index, scope.row)">删除
        </el-button>
        <el-button
          size="mini"
          type="warning"
          icon="el-icon-edit"
          @click="clickEdit(scope.$index, scope.row)">编辑
        </el-button>
        <el-dialog title="编辑用户信息" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <!-- <el-form-item label="用户密码" :label-width="formLabelWidth">
            <el-input v-model="form.password" autocomplete="off"></el-input>
          </el-form-item> -->
          <el-form-item label="用户类型" :label-width="formLabelWidth">
            <el-select v-model="form.type" placeholder="请选择用户类型">
              <!-- <el-option label="管理员" value="0"></el-option> -->
              <el-option label="地质勘探员" value="1"></el-option>
              <el-option label="普通用户" value="2"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="用户区域" :label-width="formLabelWidth">
             <el-select v-model="form.area" placeholder="请选择所在区域" :disabled="Display()">
              <el-option
                v-for="item in cities"
                :key="item.area"
                :label="item.area"
                :value="item.area">
                <span style="float: left">{{ item.area }}</span>
                <!-- <span style="float: right; color: #8492a6; font-size: 13px"></span> -->
              </el-option>
            </el-select>
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
  
  <div class="block" style=" background-color: #fff;position:absolute;bottom: 10px;left:0px;right: 0px;">
    <el-pagination
      background
      layout="total, sizes, prev, pager, next, jumper"
      :total="pageInfo.pageTotal"
      :page-sizes="[ 10, 8, 5]"
      :page-size="pageInfo.pageSize"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="pageInfo.currentPage">
    </el-pagination>
  </div>
</div>
  
</template>

<script>
  import { mapState } from 'vuex'; 
  export default {
    data() {
      return {
      forbidDisplay:true,
      //分页
      pageInfo: {
        currentPage: 1,
        pageSize: 10, //每页的初始数量
        pageTotal: 2, //总页数
      },
      inputName:'',
      userData:[],
      dialogFormVisible: false,
      form: {
        uid:'',
        name: '',
        password: '',
        type: '',
        area: '----',
        IDName: '',
        ID: ''
      },
      formLabelWidth: '120px'  ,
      cities:[]    
      }

    },
    computed:{
      ...mapState(['data'])
    },
    mounted(){
      this.QueryUser();
      this.GetAllArea();
    },
    methods: {
      handleSizeChange(val) {
        //pageSize 改变时会触发
        this.pageInfo.pageSize = val
      },
      handleCurrentChange(val) {
        //currentPage 改变时会触发
        this.pageInfo.currentPage = val
      },
      //获得所有area
      GetAllArea(){
        this.axios({
                  method: 'get',
                  url: `http://localhost:8080/api/v1/areas`,
                })
              .then(res=>{
                this.cities=res.data;
                console.log(res)
                })
              .catch(err => {
                console.log(2)
                console.log(err)
              })
      },
      // type格式化
      typeFormat (row) {
        let showProp = "普通用户"
        if (row.type == "0"){
          showProp = "管理员"
        }
        else if(row.type=="1"){
          showProp = "地质勘探员"
        }
        else{
          showProp = "普通用户"
        }
        return showProp
      },
      // 地区格式化
      areaFormat (row) {
        let showProp = null
        row.area ? showProp = row.area : showProp = '----'
        return showProp
      },
      //根据用户名模糊查询用户
      QueryInfo(name) {
        // console.log(name)
        if(name===""){
          this.QueryUser();

        }
        else{
            this.axios({
                  method: 'get',
                  url: `http://localhost:8080/api/v1/info_name`+"/"+name,
                })
              .then(res=>{
                this.userData=res.data;
                this.pageInfo.pageTotal = this.userData.length //根据数据量显示页数
                console.log(res.data)
                console.log(res.status)
                console.log(res)
                })
              .catch(err => {
                console.log(2)
                console.log(err)
              })
        }
      }
    
  ,
      //查询所有用户
      QueryUser() {
        this.axios.post('allusers')
          .then(res => {
            if (res.status === 200) {
              console.log(res);
              this.userData=res.data;
              this.pageInfo.pageTotal = this.userData.length //根据数据量显示页数
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
            var uid=this.form.uid;
            var type=this.form.type;
            
            var area=this.form.area;
            console.log("area:"+area)
            if(type!=='1'){
              area = "----"
            }
            if(area == null || area == ""){
              area = "----"
            }
        this.dialogFormVisible = false;
        this.axios.post('setinfo_type_area', {
            uid: uid,
            type: type,
            area:area
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
        if(row.type===0){
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
              // console.log("index:"+index);
              this.$message.success(res.data)
              this.QueryUser();
              // this.userData.splice(index-1,1);
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
      },
      Display(){
        
        if(this.form.type =='1'){
          return false;
        }
        else{
          this.form.area = "----";
          return true;
        }
      }
    }
  }
</script>
<style lang="less" scoped>
@import '../../../static/css/clear';
@import '../../../static/css/common';
.survey_content2{
   width: 100%;
  height: 100%;
  .body{
    height: 100%;
  }
  .contents{
  background-color: #fff;
  // background-color: rgb(198, 219, 212);
  margin: 0px 0px 0px 20px;
  padding: 0px;
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

