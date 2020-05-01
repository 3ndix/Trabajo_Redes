<template lang="html">
  <div class="container">

    <div class="row">
      <div class="col text-left">
        <h2>Editar Usuario</h2>
      </div>
    </div>

    <div class="row">
      <div class="col text-left">
        <div class="card">
          <div class="card-body">

            <form @submit="onSubmit">

              <div class="form-group row">
                <label for="rut" class="col-sm-2 col-form-label">Rut</label>
                <div class="col-sm-6">
                    <input type="text" placeholder="Ingrese Rut" name="rut" class="form-control" v-model.trim="form.rut">
                </div>
              </div>

              <div class="form-group row">
                <label for="nombres" class="col-sm-2 col-form-label">Nombres</label>
                <div class="col-sm-6">
                    <input type="text" placeholder="Ingrese Nombres" name="nombres" class="form-control" v-model.trim="form.nombres">
                </div>
              </div>

              <div class="form-group row">
                <label for="ap_paterno" class="col-sm-2 col-form-label">Apellido Paterno</label>
                <div class="col-sm-6">
                    <input type="text" placeholder="Ingrese Apellido" name="ap_paterno" class="form-control" v-model.trim="form.ap_paterno">
                </div>
              </div>

              <div class="form-group row">
                <label for="ap_materno" class="col-sm-2 col-form-label">Apellido Materno</label>
                <div class="col-sm-6">
                    <input type="text" placeholder="Ingrese Apellido" name="ap_materno" class="form-control" v-model.trim="form.ap_materno">
                </div>
              </div>
              <div class="form-group row">
                <label fro="genero" class="col-sm-2">Género</label>
                <div class="form-row align-items-center">
                  <div class="col-auto my-1">
                    <select class="custom-select mr-sm-3" id="inlineFormCustomSelect" v-model.trim="form.genero">
                      <option value="F">Femenino</option>
                      <option value="M">Masculino</option>
                      <option value="ND">Prefiero no elegir</option>
                    </select>
                  </div>
                </div>
              </div>
              <label></label>
              <div class="rows">
                <div class="col text-left">
                  <b-button type="submit" variant="primary">Guardar</b-button>
                  <b-button type="submit" btn="btn-large-space" :to="{ name: 'UserList' }">Salir</b-button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'
export default {
  data() {
    return {
      userId: this.$route.params.userId,
      form: {
        rut: '',
        nombres: '',
        ap_paterno: '',
        ap_materno: '',
        genero: ''
      }
    }
  },
  methods: {
    onSubmit(evt){
      evt.preventDefault()
      const path = 'http://localhost:8000/api/v1.0/users/'+this.userId+'/'

      axios.put(path, this.form).then((response) => {
        this.form.rut = response.data.rut
        this.form.nombres = response.data.nombres
        this.form.ap_paterno = response.data.ap_paterno
        this.form.ap_materno = response.data.ap_materno
        this.form.genero = response.data.genero

        swal("Usuario actualizado exitosamente!", "", "success")

      this.$router.push('/users');
      })
      .catch((response) => {
        swal("El RUT es inválido", "", "error")
      })
    },
    getUser (){
      const path = 'http://localhost:8000/api/v1.0/users/'+this.userId+'/'

      axios.get(path).then((response) => {
        this.form.rut = response.data.rut
        this.form.nombres = response.data.nombres
        this.form.ap_paterno = response.data.ap_paterno
        this.form.ap_materno = response.data.ap_materno
        this.form.genero = response.data.genero
      })
      .catch((response) => {
        console.log(error)
      })
    }
  },
  created(){
    this.getUser()
  },
}
</script>

<style lang="css" scoped>
</style>
