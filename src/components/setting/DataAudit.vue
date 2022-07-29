<template>
<div class="survey_content2 clearfix">
  <!-- <p>当前用户的token为：{{data}}</p> -->
  <!-- <el-button class='right' type="success" size="small" @click='add'>添加用户</el-button> -->
  <div class="contents clearfix">    
    <el-table :data="tagData.slice(
        (pageInfo.currentPage - 1) * pageInfo.pageSize,
        pageInfo.currentPage * pageInfo.pageSize
      )" style="width: 100%" :default-sort = "{prop: 'eid', order: 'ascending'}" >
    <el-table-column prop="eid" sortable label="标记ID" width="150"></el-table-column>
    <el-table-column prop="uid" label="UID"  width="100"></el-table-column>

    <!-- <el-table-column prop="password" label="用户密码"></el-table-column> -->
    <el-table-column prop="time" :formatter="timeFormat" label="提交时间">
    <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px" >{{ scope.row.time.replace('T',' ') }}</span>
      </template>
    </el-table-column>
    <el-table-column prop="title" label="标题"></el-table-column>
    <el-table-column prop="tag_sesc" label="描述"></el-table-column>
    <el-table-column prop="enentype" label="类型">
        <template slot-scope="scope">
            <el-tag size="medium">{{ scope.row.enentype }}</el-tag>
        </template>
        
    </el-table-column>
    <!-- <el-table-column prop="add" label="创建时间" sortable></el-table-column>
    <el-table-column prop="change" label="修改时间" sortable></el-table-column> -->
    <el-table-column label="详细信息" width="150">
      <template slot-scope="scope">

        <el-button
          size="mini"
          type="warning"
          @click="clickEdit(scope.$index, scope.row)">详情
        </el-button>
        <el-dialog title="标记信息" :visible.sync="dialogFormVisible">
        <el-form :model="form">
        <el-descriptions class="margin-top" title="标记详情" :column="3" :size="size" border>
            <template slot="extra">
                <el-button :disabled="btnChangeEnable" type="success" @click="auditSuc(form.eid)" size="small">审核通过</el-button>
                <el-button :disabled="btnChangeEnable" type="danger" @click="auditErr(form.eid)" size="small">审核失败</el-button>
            </template>

            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-user"></i>
                用户ID 
            </template>
            {{form.uid}}
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-s-grid"></i>
                标记标题
            </template>
            {{form.title}}
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-tickets"></i>
                标记描述
            </template>
            {{form.tag_sesc}}
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-more"></i>
                标记类型
            </template>
            <el-tag size="small">{{form.enentype}}</el-tag>
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-location-outline"></i>
                经度
            </template>
            {{form.lng}}
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-location-information"></i>
                纬度
            </template>
            {{form.lat}}
            </el-descriptions-item>
            <el-descriptions-item>
            <template slot="label">
                <i class="el-icon-date"></i>
                提交时间
            </template>
            {{form.time.replace('T',' ')}}
            </el-descriptions-item>
            <el-descriptions-item>
                <template slot="label">
                <i class="el-icon-picture-outline"></i>
                标记图片
                </template>
                <div class="demo-image__placeholder">
                    <div class="block">
                        <el-image style="width: 100px; height: 100px" :src=form.imgSrc :fit="fill" :preview-src-list=[form.imgSrc]>
                        <div slot="placeholder" class="image-slot">
                            加载中<span class="dot">...</span>
                        </div>
                        </el-image>
                    </div>
                </div>
            </el-descriptions-item>
        </el-descriptions>

        </el-form>

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
<div class="block" style="  margin-bottom: 0px;background-color: #fff;">
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
        //分页
      pageInfo: {
        currentPage: 1,
        pageSize: 10, //每页的初始数量
        pageTotal: 6, //总页数
      },
      btnChangeEnable: false,
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
      handleSizeChange(val) {
        //pageSize 改变时会触发
        this.pageInfo.pageSize = val
      },
      handleCurrentChange(val) {
        //currentPage 改变时会触发
        this.pageInfo.currentPage = val
      },
    //审核成功
        auditSuc(eid){
            console.log(eid)
            this.axios.post('finishaudit',{
                "eid": eid,
                "auditStatus": 1
            })
            .then(res=>{
                console.log(res)
                this.$message.success('审核成功')
                //审核完成后不可点击
                this.btnChangeEnable=true
                this.QueryTag();
            })
            .catch(err=>{
                this.$message.error('审核出现问题')
            })
        },
    //审核失败
        auditErr(eid){
            this.axios.post('finishaudit',{
                "eid": eid,
                "auditStatus": -1
            })
            .then(res=>{
                console.log(res)
                this.$message.success('已提交审核结果')
                //审核完成后不可点击
                this.btnChangeEnable=true
                this.QueryTag();

            })
            .catch(err=>{
                this.$message.error('审核出现问题')
            })
        },
    // 时间类型格式化
      timeFormat (row) {
        row.time  = row.time.replace('T',' ')
        return row.time
      },
      //查询所有标记
      QueryTag() {
        console.log("type:"+this.$store.state.data.type)
        var type = this.$store.state.data.type;
        if(type=='1')
        {
        var area = this.$store.state.data.area;
        this.axios.post('areainformaltags/'+area)
          .then(res => {
            if (res.status === 200) {
              console.log(res);
              this.tagData=res.data;
              this.pageInfo.pageTotal = this.tagData.length //根据数据量显示页数

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
        }
        else{
            this.axios.post('areainformaltags'+"/全部")
            .then(res => {
                if (res.status === 200) {
                console.log(res);
                this.tagData=res.data;
                this.pageInfo.pageTotal = this.tagData.length //根据数据量显示页数

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
        }
      },
      //点击编辑按钮
      clickEdit(index, row) {
        this.btnChangeEnable=false;
        this.form.uid=row.uid;
        this.form.eid=row.eid;
        this.form.enentype=row.enentype;
        this.form.time=row.time;
        this.form.lng=row.lng;
        this.form.lat=row.lat;
        this.form.area=row.area;
        this.form.title=row.title;
        this.form.tag_sesc=row.tag_sesc;
        this.form.imgSrc=row.imgSrc;
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
  height: 95.5%;
  }
  .right{
    // height: 30px;
    position: absolute;
    right: 20px;
    top: 20px;
  }

}
</style>

