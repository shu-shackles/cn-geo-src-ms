import {test} from "../test.js"
<template>
    <div class="registerContainer">
        <div class="register">
            <p>欢迎注册</p>
            <el-form ref="form" :model="form"  label-width="80px" status-icon :rules="rules">
            
                <el-form-item style="width: 420px;" label="用户名" prop="username">
                    <el-input style="width: 320px;" v-model="form.username"  placeholder="请输入用户名" autocomplete="off">
                      <i slot="prefix" class="el-icon-user"></i>
                    </el-input>
                </el-form-item>

                <el-form-item style="width: 420px;" label="密码" prop="password">
                    <el-input style="width: 320px;" type="password" v-model="form.password" placeholder="请输入密码" autocomplete="off">
                      <i slot="prefix" class="iconfont icon-lock"></i>
                    </el-input>
                </el-form-item>

                <el-form-item style="width: 420px;" label="确认密码" prop="check_pass ">
                    <el-input style="width: 320px;" type="password" v-model="form.check_pass"  placeholder="请再次输入密码" autocomplete="off">
                      <i slot="prefix" class="iconfont icon-lock"></i>
                    </el-input>
                </el-form-item>

                <el-form-item  style="width: 420px;" label="姓名" prop="IDNAME">
                  <el-input id="CardIDName"  :disabled="false" style="width: 320px;" v-model="form.IDNAME"  placeholder="请输入姓名" autocomplete="off">
                    <i slot="prefix" class="el-icon-s-custom"></i>
                  </el-input>
                </el-form-item>

                <el-form-item  style="width: 520px;" label="身份证号" prop="ID">
                    <el-input id="CardID" :disabled="false"  style="width: 320px;" v-model="form.ID" placeholder="请输入18位身份证号" autocomplete="off">
                      <i slot="prefix" class="el-icon-s-check"></i>
                    </el-input>
                    <el-button  style="width: 100px;height: 50px;margin-left: 10px;padding: 4% 4%;" type="success" @click="submitID('form')">身份审核</el-button>
                </el-form-item>
              <el-form>
                <el-form-item>
                    <el-button type="primary" @click="submitForm('form')">提交</el-button>
                    <el-button type="info" @click="resetForm('form')">重置</el-button>
                </el-form-item>
              </el-form>
              <el-form  style="margin-bottom:0px;"> 
                        <el-form-item style="margin-bottom:0px;">
                          <span style="color:black;font-size:16px">已有账号</span>
                          <a data-v-a1217096="" @click="onLogin" class="el-link el-link--success" style="height: 46px;">
                          <span class="el-link--inner" style="height: 46px;font-size: 16px;">立即登录</span>
                          </a>
                        </el-form-item>
              </el-form>  

            </el-form>
        </div>

    </div>

</template>

<script>

  export default {
    name: '',
    data(){
      let checkname=(rule,value,callback)=>{
        if(!value){
          return callback(new Error('请输入用户名 '))
        }else{
          callback()
        }
      };
      let validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.form.check_pass !== '') {
            this.$refs.form.validateField('check_pass');
          }
          callback();
        }
      };
      let validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.form.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return{
        IDValid:false,
        form:{
          username:'',
          password:'',
          check_pass:'',
          ID:'',
          IDNAME:''
        },
        rules:{
          username:[
            {validator:checkname, trigger: 'blur',required: true}
          ],
          IDNAME:[
            { required: true, message: '请输入姓名', trigger: 'blur' ,required: true}
          ],
          ID:[
              { required: true, message: '请输入身份证号', trigger: 'blur' ,required: true},
              { min:18,max:18, message: '输入的身份证号有误', trigger: 'blur' }
          ],
          password:[
            {validator:validatePass,trigger:'blur',required: true},
            { min: 6, max: 20, message: '密码长度在6-20个字符之间', trigger: 'blur' }
          ],
          check_pass:[
            {validator:validatePass2 ,trigger:'blur',required: true}
          ]
        }
      }
    },
    methods:{
      //提交注册
      submitForm(formName){
        this.$refs[formName].validate((valid)=>{
          console.log(this.IDValid)
          if(!this.IDValid){
            this.$alert('身份认证失败: 请确认输入信息',{type:"error"})
          }
          if(valid && this.IDValid){
            console.log(this.form);
            this.axios.post('/register',this.form)
              .then(res=>{
                console.log(res)
                if(res.status===200 ){
                  //element的消息框提示
                  this.$message.success('注册成功,即将跳转到登录界面！',{center:true})
                  // this.$alert('注册成功,即将跳转到登录界面！',{center:true})
                  this.$router.push('/')
                }else{
                  // this.$message.error('注册失败: '+res.data,{center:true})
                  this.$alert('注册失败: '+res.data,{type:"error"})
                }
              })
              .catch(err=>{
                console.log(err)
              })
          }
        })
      },
      //身份审核
      submitID(forName){
        this.$refs[forName].validate((valid)=>{
          if(valid){
            this.axios({
              method: 'get',
                url: `http://localhost:8080/api/v1/IDAuthen`,
                params: { 
                  cardID : this.form.ID,
                  realName : this.form.IDNAME 
                }
            })
            .then(res=>{
              console.log(res.data)
              console.log(res.status)
              console.log(res)
              if(res.data.result==="1"){
                this.IDValid = true;
                console.log(this.IDValid);
                //身份核验成功后身份信息不可更改
                document.getElementById("CardID").setAttribute("readonly",true);
                document.getElementById("CardIDName").setAttribute("readonly",true);
                this.$alert('身份核验成功:！',{type:"success"});
              }
              else{
                this.IDValid = false;
                console.log(this.IDValid);
                this.$alert('身份核验失败，请重试！',{type:"error"});
              }
            })
          
          }
        })

      },
      //重置表单
      resetForm(formName){
        this.$refs[formName].resetFields()
      },
      onLogin(){
        //已有账号立即登录
        this.$router.push('/')
      }
    
    }


  }
</script>

<style  lang="less" scoped>
.registerContainer{
    display:flex;
    justify-content:center;
    align-items:center;
    width:100%;
    margin:auto;
    /*height:650px;*/
    .register{
      width: 500px;
      height: 320px;
      margin: 100px auto;
      // width:40%;
       .el-button{
         padding: 4% 10%;
         }
       .el-button--defalut{
           float: left;;

       }
    p{
        text-align: center;
        font-size: 30px;
        margin-bottom: 30px;
    }
    }

}
</style>
