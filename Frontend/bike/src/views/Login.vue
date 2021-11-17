<template>
<div>
<Navbar/>
<div class="container">
        <div class="row justify-content-center align-items-center" style="height:100vh">
            <div class="col-4">
                <div class="card">
                    <img src="../assets/logo-bike-nome.png"  alt="Logo-rike" />
                    <div class="card-body mt-2">
                        <form @submit="login" autocomplete="off">
                            <label class="form-label mt-2">Email</label>
                                <input type="text" class="form-control " v-model="credentials.email">                            
                                <label class="form-label mt-2">Password</label>
                                <input type="password" class="form-control" v-model="credentials.password">
                            <button type="button" id="sendlogin" class="btn btn-primary mt-2">login</button>
                            
                        </form>
                        <a class="text-muted text-center" href="/createuser">Create new user</a>
                            <router-link to="/createuser" active-class="active" exact></router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>

</template>

<script>
import axios from "axios";
import Navbar from "../components/Navbar.vue";
export default {
    components:{
            Navbar
        },
    data(){
        
        return{
            credentials:{
                email:"",
                password:""
            }
        }
    },
    methods:{
        async login(){
            await axios.post("http://127.0.0.1:8000/login", this.credentials);
        }
    }
}
</script>