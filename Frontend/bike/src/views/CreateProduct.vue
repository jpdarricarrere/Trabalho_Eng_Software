<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-4">
        <div class="card">
            <img src="../assets/logo-bike-nome.png"  alt="Logo-rike" />
        <div class="card-body mt-2 py-2">
            <form @submit.prevent="create">
            <label class="form-label mt-2" >Nome da bicicleta</label>
            <input type="text" class="form-control" v-model="bike.nome" > 
            <label class="form-label mt-2" >Tipo da bicicleta</label>
            <input type="text" class="form-control" v-model="bike.tipo" > 
            <label class="form-label mt-2" >Modelo</label>
            <div class="row">
           <select v-model="bike.modelo" class="py-2">
                <option>Mountain Bike</option>
                <option>Speed</option>
                <option>Urbana</option>
                <option>Eletrica</option>
            </select> 
            <label class="form-label mg-2" >Numero de marchas</label>
            <input type="text" class="form-control" v-model="bike.num_marchas" > 
            <label class="form-label mt-2" >Tamanho do Aro</label>
            <input type="text" class="form-control"  v-model="bike.aro"> 
            </div>
            <label class="form-label mt-2" >Link da Imagem</label>
            <input type="text" class="form-control" v-model="bike.link_imagem" > 
            <label class="form-label mt-2" >Ano</label>
            <input type="text" class="form-control" v-model="bike.ano" > 
            <button type="submit" class="btn btn-primary mt-2">Cadastrar Bicicleta</button>
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
    data(){
        return{
            bike:{
                nome:"",
                modelo:"Speed",
                link_imagem:"",
                tipo:"",
                num_marchas:1,
                ano:1,
                aro:1,
                id_adm:1
            }
        }
    },
    methods:{
        create(){
            console.log(this.bike);
            axios.post("http://127.0.0.1:8000/bikes", this.bike);
            //axios.push("/")
        }
    }
}
</script>