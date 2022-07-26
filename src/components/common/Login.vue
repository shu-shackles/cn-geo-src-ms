<template>
    <div class="loginContainer">
        <div class="login">
            <p>中国地质资源管理系统</p>
            <p>用户登录</p>
            <!--element的form表单-->
            <div class="login-content">
                <el-form  :label-position="right" :model="formLabelAlign"
                        :rules="rules" ref="formLabelAlign" status-icon  label-width="70px">

                    <el-form-item label="用户名" prop="username">
                        <el-input  v-model="formLabelAlign.username"
                                  placeholder="请输入用户名"  autocomplete="on" >
                            <i slot="prefix" class="iconfont icon-my"></i>
                        </el-input>
                    </el-form-item>

                    <el-form-item label="密码" prop="password">
                        <el-input type="password" v-model="formLabelAlign.password" placeholder="请输入密码"
                                  autocomplete="off">
                            <!--阿里字体，slot是element的控制图标位置的-->
                            <i slot="prefix" class="iconfont icon-lock"></i>
                            <!-- <i slot="suffix" class="iconfont icon-display"></i> -->
                        </el-input>
                    </el-form-item>

                    <el-form style="margin-bottom:10px;"> 
                        <el-form-item style="margin-bottom:0px;">
                          <el-button type="primary" round @click="onSubmit('formLabelAlign')">登录</el-button>
                        </el-form-item>
                    </el-form>

                    <el-form  style="margin-bottom:0px;"> 
                        <el-form-item style="margin-bottom:0px;">
                          <span style="color:black;font-size:16px">没有账号</span>
                          <a data-v-a1217096="" @click="onRegister" class="el-link el-link--success" style="height: 46px;">
                          <span class="el-link--inner" style="height: 46px;font-size: 16px;">立即注册</span>
                          </a>
                        </el-form-item>
                    </el-form>
                    <!-- <slide-verify :l="42"
                      :r="10"
                      :w="310"
                      :h="155"
                      slider-text="向右滑动"
                      @success="onSuccess"
                      @fail="onFail"
                      @refresh="onRefresh"
                    ></slide-verify>
                    <div>{{msg}}</div> -->
                </el-form>

            </div>
        </div>

    </div>
</template>

<script>
  import {mapState} from 'vuex'
  export default {
    data () {
      //element表单校验
      let checkname=(rule,value,callback)=>{
        if(!value){
          return callback(new Error('请输入用户名 '))
        }else{
          callback()
        }
      }
      let checkpass=(rule,value,callback)=>{
        if(!value){
          return callback(new Error('请输入密码'))
        }else{
          callback()
        }
      }
      return {
        msg:'',
        labelPosition: 'right',
        formLabelAlign: {
          username: '',
          password: ''
        },
        rules: {
          username: [
            // {required: true, message: '请输入用户名', trigger: 'blur'}
            {validator:checkname, trigger: 'blur'}
          ],
          password: [
            {validator:checkpass, trigger: 'blur'}
            // {min: 5, max: 20, message: '长度在5到20个字符', trigger: 'blur'}
          ]
        }
      }
    },
    created () {
      // this.islogin()
    },
    computed:{
      ...mapState(['token'])
    },
    methods: {
      //判断是否登录，已登录则跳转到主页
      islogin(){
        if (this.$store.state.user) {
          this.$router.push('/home')
        }
      },
      //提交valid验证后的表单，发送请求，调用接口，
      onSubmit (formName) {
          this.$refs[formName].validate((valid)=> {
            if (valid) {
              this.axios.post('login_access', "grant_type=&username="+this.formLabelAlign.username+
                    "&password="+this.formLabelAlign.password+"&scope=&client_id=&client_secret=")
                    .then(res => {
                      if (res.status === 200) {
                        console.log(res)
                        window.sessionStorage.setItem('userToken', res.data.access_token)
                        this.$store.state.token=res.data.access_token
                        console.log("当前token为: "+this.$store.state.token)
                        console.log()
                        this.$message.success('登录成功')
                        this.$router.push('/index')
                        this.axios({
                          method: 'post',
                          url: 'login_get_user',
                          headers: {'Authorization':"Bearer "+this.token
                            }
                          })
                        .then(res=> {
                            //handle success
                            window.sessionStorage.setItem('uid', res.data[0].uid)
                            window.sessionStorage.setItem('name', res.data[0].name)
                            window.sessionStorage.setItem('password', res.data[0].password)
                            window.sessionStorage.setItem('type', res.data[0].type)
                            window.sessionStorage.setItem('area', res.data[0].area)
                            window.sessionStorage.setItem('ID', res.data[0].ID)
                            window.sessionStorage.setItem('IDName', res.data[0].IDName)
                            window.sessionStorage.setItem('data',JSON.stringify(res.data[0]))
                            this.$store.state.data = res.data[0]
                            console.log(res);
                            console.log(res.data[0].uid)
                            console.log(this.data)
                            // console.log(this.name+this.password+this.area+this.type+this.ID+this.IDName)
                            
                        })
                        .catch(function (response) {
                            //handle error
                            console.log("error:"+response);
                        });

                      }else{
                        console.log(res)
                        this.$message.error('token返回失败: ')
                        // this.$refs[formName].resetFields()
                      }
                    })
                    .catch(err => {
                      console.log("出现错误："+err)
                    })
              console.log("token:"+this.token)
            }
            
          })
        },
      //注册
      onRegister(){
        this.$router.push('/register')
      },
      onSuccess(){
        this.msg = 'login success'
      },
      onFail(){
        this.msg = 'login failed'
      },
      onRefresh(){
        this.msg = 'refresh'
      }

      }

  }
</script>


<style lang="less" scoped >
    // @import "../assets/fonts/iconfont.css";
    .loginContainer{
         display:flex;
        //  justify-content:center;
         align-items:center;
         width:100%;
         height:100%;
         background: url('../../assets/images/g.jpg') no-repeat center;
        -webkit-background-size:cover ;
        background-size: cover;

         .login{
             align-items:center;
             width: 450px;
             height: 320px;
             // margin-left: 100px;
             background-color: white;
             border-radius: 2%;
             padding: 15px 50px 15px 50px;
             color: #ffffffc4;
             margin:0 auto;
         }
        p{
            width: 100%;
            padding-left:0px;
            margin-bottom: 10px;
            font-size: 20px;
            text-align: center;
            color:black;
        }
        .login-content{
        .el-button{
            padding: 11px 44px;
        }
        .iconfont{
           font-size: 15px;
        }

        }
    }

</style>
<style>

    .login-content .el-form-item__label{
         color: #606266
;
     }


</style>
