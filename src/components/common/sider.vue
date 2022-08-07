<template>
    <div class="sider">
        <!-- <div @click="showMenus()" class="sum">
            <i class="iconfont icon-liebiao navi "></i>
        </div> -->
        <div class="navigator" v-if="showMenu">
            <el-menu router :default-active="$route.name" class="el-menu-vertical-demo" text-color="#fff"
                background-color="#1B467B" active-text-color="#ffd04b">
                <div class="ava">
                    <img class="avator" src='@/assets/images/logo.png'>
                    <div class="name">
                        <div>欢迎您</div>
                        <div style="text-align:center;cursor: pointer;" @click='centerDialogVisible = true'>
                            {{ $store.state.data.name }}</div>
                    </div>
                    <el-dialog :modal-append-to-body="false" title="修改密码" :visible.sync="centerDialogVisible"
                        width="30%" center>
                        <el-form ref="form" status-icon :model="form" :rules="rules">
                        <el-form-item label="密码" prop="password">
                        <el-input  type="password" v-model="form.password" placeholder="请输入密码" autocomplete="off">
                            <i slot="prefix" class="iconfont icon-lock"></i>
                            </el-input>
                        </el-form-item>

                        <el-form-item  label="确认密码" prop="check_pass">
                            <el-input  type="password" v-model="form.check_pass" @input="complete"  placeholder="请再次输入密码" autocomplete="off">
                            <i slot="prefix" class="iconfont icon-lock"></i>
                            </el-input>
                        </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
                            <el-button @click="unChangePW()">取 消</el-button>
                            <el-button type="primary" @click="changePW()">确 定</el-button>
                        </span>
                    </el-dialog>
                    <div class=" btns" @click='backIndex()'>主页</div>
                    <div class="avatorBtn" @click='backLogin()'>退出</div>
                </div>
                <label v-for="item in menu" :key="item.titleIndex">
                    <el-submenu :index="item.titleIndex">
                        <template slot="title">
                            <i :class="item.icon"></i>
                            <span>{{ item.title }}</span>
                        </template>
                        <template v-for="ele in item.levelInfo">
                            <el-menu-item v-if="!ele.levelInfo" @click.native="changeTitle(ele.levelIndex)"
                                :index="ele.levelIndex" :key="ele.levelIndex" :route="ele.path">{{ ele.level }}
                            </el-menu-item>
                            <el-submenu v-else :index="ele.titleIndex">
                                <template slot="title">{{ ele.level }}</template>
                                <el-menu-item v-for="data in ele.levelInfo" @click.native="changeTitle(data.levelIndex)"
                                    :index="data.levelIndex" :key="data.levelIndex" :route="data.path">{{ data.level }}
                                </el-menu-item>

                            </el-submenu>

                        </template>

                    </el-submenu>
                </label>
            </el-menu>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import * as consts from '../../common/const'
import axios from 'axios'
export default {
    data() {
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
        return {
            centerDialogVisible: false,
            showMenu: true,
            menu: {},
            type: -1,
            form:{
                password: '',
                check_pass: ''
            },
            rules:{
                password:[
                    {validator:validatePass,trigger:'blur'},
                    { min: 6, max: 20, message: '密码长度在6-20个字符之间', trigger: ['blur', "change"] }
                ],
                check_pass:[
                    {validator:validatePass2 ,trigger:['blur', "change"]}
                ]
            }
        }
    },
    created() {
        console.log(this.data)
        console.log(this.token)
        this.getMenu()
    },
    computed: {
        // ...mapState(['data']),
        ...mapState(['token']),
        showMenu: {
            // getter
            get: function () {
                return this.$store.state.menu.showMenu
            },
            // setter
            set: function (v) {
                this.$store.state.menu.showMenu = v
            }
        },
    },
    methods: {
     
        complete(e) {
            if(this.form.check_pass.length>=0) {
                
                e.srcElement.blur(); // 让输入框主动失焦
            }
        },


        // 导航栏显示与否
        showMenus() {
            this.showMenu = !this.showMenu
        },
        // 获取导航栏
        getMenu() {
            console.log('!!!!!!!!!', this.$store.state.token)
            var config = {
                method: 'post',
                url: 'http://localhost:8080/api/v1/login_get_user',
                headers: {
                    'Authorization': 'Bearer ' + this.$store.state.token,
                },
            };
            axios(config)
                .then(response => {
                    console.log('-----------', response.data[0].type);
                    this.type = response.data[0].type
                    if (this.type == 0) {
                        this.menu = consts.ASIDE_TITLE0
                    }
                    else if (this.type == 1) {
                        this.menu = consts.ASIDE_TITLE1
                    }
                    else if (this.type == 2) {
                        this.menu = consts.ASIDE_TITLE2
                    }
                })
                .catch(error => {
                    console.log('-----------', error);
                });
            // this.projects=this.menu.project
        },
        // 点击退出，返回到登录页面
        backLogin() {
            // this.$store.state.token = "%"
            // console.log(this.$store.state.token)
            this.$router.push({ name: 'login' })
        },
        backIndex() {
            this.$router.push({ name: 'index' })
        },
        changeTitle() { },
        unChangePW(){
            this.centerDialogVisible = false;
            this.form.password = '';
            this.form.check_pass = '';
        },
        changePW() {
            this.centerDialogVisible = false;
            var uid = this.$store.state.data.uid;
            this.axios.post('setinfopassword', {
                "password": this.form.password,
                "check_pass": this.form.check_pass,
                "uid": uid
            })
                .then(res => {
                    this.$message.success('密码修改成功！');
                    this.form.password = '';
                    this.form.check_pass = '';
                })
                .catch(err => {
                    this.$message.error('密码修改失败！');
                    this.form.password = '';
                    this.form.check_pass = '';
                })
        }

    }
}
</script>

<style lang="less" scoped>
@import '../../../static/css/clear';
@import '../../../static/css/common';

.sider {
    // position: relative;
    // float: left;
    // width:10%;
    // flex: 0.1;
    height: 100%;

    .sum {
        position: fixed;
        top: 10px;
        left: 6px;
        width: 23px;
        height: 23px;
        z-index: 999;
    }

    .navi {
        color: #999;
        font-size: 20px;

    }

    .navigator {
        position: fixed;
        top: 0;
        bottom: 0;
        z-index: 99;
        overflow: hidden;
        height: 100%;

        .ava {
            border-bottom: 0.5px solid #fff;
            position: relative;
            width: 100%;
            height: 80px;


            .avator {
                position: absolute;
                width: 70px;
                height: 70px;
                background-color: white;
                top: 5px;
                left: 5px;
                border-radius: 70%;
            }

            .name {
                position: absolute;
                right: 21px;
                top: 10px;
                font-size: 12px;
                color: #fff;
            }

            .avatorBtn {
                position: absolute;
                right: 10px;
                bottom: 10px;
                font-size: 12px;
                color: #fff;
                cursor: pointer;
            }

            .btns {
                position: absolute;

                bottom: 10px;
                right: 50px;
                font-size: 12px;
                color: #fff;
                cursor: pointer;


            }
        }
    }

    .el-submenu div:hover {
        background-color: #46988efa;
    }

    .el-menu-item-group li:hover {
        background-color: #46988efa;
    }

    .el-menu-item-group__title {
        padding: 0px;
    }

    .el-submenu .el-menu-item {
        height: 35px;
        line-height: 35px;
        min-width: 0px;
        color: #71a8e0;
        font-size: 14px;
    }

    .el-menu--inline .el-submenu__title {
        font-size: 14px;
    }

}
</style>
<style>
.el-submenu .el-submenu__title {
    margin-left: -40px;
}

.el-submenu__title i {
    color: #fff;
}

.el-submenu .el-menu-item {
    padding: 0px;
    padding-left: 0 !important;
}

.el-menu {
    width: 160px;
    /* width: 100%; */
    height: 100%;
    border: 0px solid !important
}
</style>

