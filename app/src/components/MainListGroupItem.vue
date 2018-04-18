<template>
  <b-list-group-item class="d-flex align-items-center">
    <b-container fluid class="p-0">
      <b-row align-v="center">
        <b-col cols="1">
          <i class="fa fa-link fa-lg"></i>
        </b-col>
        <b-col cols="2">
          <h4 class="m-0">{{ name }}</h4>
        </b-col>
        <b-col class="text-right">
          <b-row>
            <b-col>  
              <p class="mb-0"><small>https://galpi.io</small><b>{{ path }}</b></p>
            </b-col>
          </b-row>
          <b-row align-v="center">
            <b-col>  
              <small class="text-secondary">{{ link }}</small>
              <i class="fa fa-edit align-middle"></i>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
  </b-list-group-item>
</template>

<script>
export default {
  name: 'MainListGroupItem',
  
  props: {
    owner: {
      type: Boolean,
      required: true,
    },
    path: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    link: {
      type: String,
      default: '',
    },
  },
};
</script>
