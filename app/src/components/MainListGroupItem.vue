<template>
  <b-list-group-item class="d-flex align-items-center justify-content-between">
    <div>
      <i class="fa fa-lg" :class="icon"></i>
    </div>

    <div class="flex-fill">
      <b-container class="p-0 mx-4">
        <b-row align-h="start">
          <b-col cols="2">
            <b-link :href="absPath">
              <h4 class="d-inline m-0">{{ name }}</h4>
            </b-link>
          </b-col>
          <b-col>
            <div v-if="link">
              <b-link
                class="text-secondary"
                :href="link">
                {{ link }}
              </b-link>
            </div>
            <div v-else>
              <span class="text-secondary">
                {{ count }} {{ countUnit }}
              </span>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </div>

    <div>
      <b-dropdown variant="outline-muted" no-caret right>
        <template slot="button-content">
          <i class="fa fa-bars"></i>
        </template>
        <b-dropdown-header>
          <abbr title="You can access the item with this link">{{ absPath }}</abbr>
        </b-dropdown-header>
        <b-dropdown-divider></b-dropdown-divider>
        <div class="d-flex justify-content-end px-2">
          <b-button size="sm" variant="outline-danger">
            <i class="fa fa-trash-o"></i>
          </b-button>
          <b-button class="mx-1" size="sm" variant="outline-secondary">
            Edit
            <!-- <i class="fa fa-edit"></i> -->
          </b-button>
        </div>
      </b-dropdown>
    </div>
  </b-list-group-item>
</template>

<script>
import _ from 'lodash';

export default {
  name: 'MainListGroupItem',

  props: {
    owner: {
      type: Boolean,
      required: true,
    },
    base: {
      type: Array,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    item: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {
      showClipboard: false,
    };
  },

  computed: {
    relPath() {
      const segs = _.concat(this.base, this.name);
      return _.join(segs, '/');
    },
    absPath() {
      return `${process.env.APP_BASE_URL}/${this.relPath}`;
    },
    link() {
      return _.get(this.item, 'link', '');
    },
    count() {
      const subs = _.get(this.item, 'subs', {});
      return _.size(subs);
    },
    countUnit() {
      return this.count < 2 ? 'item' : 'items';
    },
    isFolder() {
      return this.link === '';
    },
    icon() {
      return this.isFolder ? 'fa-folder-o' : 'fa-link';
    },
  },
};
</script>
