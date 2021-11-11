<template>
<div class="container">
        <div class="row justify-content-center " style="height:100vh">
            <div class="col-4">
                <div class="card">
                    <img src="../assets/logo-bike-nome.png"  alt="Logo-rike" />
                    <div class="card-body mt-2">
                        <form @submit="create" autocomplete="off">
                            <label class="form-label mt-2">Nome Completo</label>
                                <input type="text" class="form-control " v-model="credentials.nome" placeholder="Guilherme Santana">                            
                                <label class="form-label mt-2">Email</label>
                                <input type="text" class="form-control " v-model="credentials.email" placeholder="exemplo@exemplo.com.br">  
                                <label class="form-label mt-2">Senha</label>    
                                <input type="password" class="form-control" v-model="credentials.password">
                                <label class="form-label mt-2">Confirme sua senha</label>    
                                <input type="password" class="form-control" v-model="credentials.confirm_password">
                            <button type="submit" class="btn btn-primary mt-2">Create</button>
                        </form>
                       
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from "axios";

export default {
    name: "Create",
    data(){
        return{
            credentials:{
            nome:"",
            email:"",
            password:"",
            confirm_password:"",
            }
        };
    },
    methods: {
        async create(){
            try{
                if(this.password==this.confirm_password){
                    await axios.post("api/users/", this.credentials);
                    this.$router.push("/");

                }
            }
            catch(error){
                console.log(error);
            }

        }
    }
}
</script>