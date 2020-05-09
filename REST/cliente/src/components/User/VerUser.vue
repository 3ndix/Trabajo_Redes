<template lang="html">
    <div class="container">
      <div class="row">
        <div class="col text-left">

          <h2>Datos de usuario</h2>
          <p>Rut : {{this.element.rut}}</p>
          <p>Nombres : {{ this.element.nombres }}</p>
          <p>Appellido Paterno : {{this.element.ap_paterno}}</p>
          <p>Appellido Materno : {{this.element.ap_materno}}</p>
          <p>Género : {{this.element.genero}}</p>

        </div>
      </div>
      <div class="row">
        <div class="col">
          <b-button type="submit" v-on:click="saludar" variant="primary">
            Saludar
          </b-button>
          <b-button variant="primary" :to="{ name: 'EditUser' }">
            Editar
          </b-button>
          <b-button variant="primary" :to="{ name: 'UserList' }">
            Salir
          </b-button>
          <b-button v-on:click="eliminar" variant="danger">
            Eliminar
          </b-button>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'
export default {
  data () {
    return {
      userId: this.$route.params.userId,
      element: {
        rut: '',
        nombres: '',
        ap_paterno: '',
        ap_materno: '',
        genero: ''
      },
    }
  },
  methods: {
    saludar: function (event) {
      const path = 'http://localhost:8000/api/v1.0/users/'+this.userId+'/'

      axios.get(path).then((response) => {
        this.element.rut = response.data.rut
        this.element.nombres = response.data.nombres
        this.element.ap_paterno = response.data.ap_paterno
        this.element.ap_materno = response.data.ap_materno
        this.element.genero = response.data.genero
        if (this.element.genero=="M"){
          swal({
            title: "Hola Sr."+" "+this.element.nombres+" "+this.element.ap_paterno+" "+this.element.ap_materno,
          })
        }
        if (this.element.genero=="F"){
          swal({
            title: "Hola Sra."+" "+this.element.nombres+" "+this.element.ap_paterno+" "+this.element.ap_materno,
          })
        }
        if (this.element.genero=="ND"){
          swal({
            title: "Hola "+" "+this.element.nombres+" "+this.element.ap_paterno+" "+this.element.ap_materno,
          })
        }
      })
    },
    getUser () {
      const path = 'http://localhost:8000/api/v1.0/users/'+this.userId+'/'

      axios.get(path).then((response) => {
        this.element.rut = response.data.rut
        this.element.nombres = response.data.nombres
        this.element.ap_paterno = response.data.ap_paterno
        this.element.ap_materno = response.data.ap_materno
        this.element.genero = response.data.genero
      })
      .catch((response) => {
        console.log(error)
      })
    },
    eliminar: function (event) {
      swal({
        title: "¿Estás seguro?",
        text: "Una vez borrado no se podra recuperar!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          const path = 'http://localhost:8000/api/v1.0/users/'+this.userId+'/'

          axios.delete(path).then((response) => {
            location.href = '/users'
          })
          .catch((error) => {
            swal("No es posible eliminar el Usuario", "", "error")
          })
          swal("Usuario eliminado exitosamente!", "", "success")
          this.$router.push('/users');
        }
      })
    }
  },
  created() {
    this.getUser()
  }
}
</script>

<style lang="css" scoped>
</style>
