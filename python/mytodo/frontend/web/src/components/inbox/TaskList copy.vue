<template>
  <v-card max-width="500" class="mx-auto">
    <v-toolbar color="primary" dark>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Inbox</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-checkbox-marked-circle</v-icon>
      </v-btn>
    </v-toolbar>

    <v-list two-line>
      <v-list-item-group v-model="selected">
        <template v-for="(item, index) in items">
          <v-list-item :key="item.title" :disabled="!inEditMode(index) && selected >= 0">
            <template v-slot:default="{active}">
              <v-list-item-content>
                <v-list-item-title v-if="inEditMode(index)">
                  <v-text-field label="Title" :value="item.title"></v-text-field>
                </v-list-item-title>
                <v-list-item-title v-else v-text="item.title"></v-list-item-title>

                <v-list-item-subtitle>
                  <v-chip x-small class="ma-2" color="primary">Primary</v-chip>
                  <v-chip x-small class="ma-2" color="secondary">Secondary</v-chip>
                  <v-chip x-small class="ma-2" color="red" text-color="white">Red Chip</v-chip>
                  <v-chip x-small class="ma-2" color="green" text-color="white">Green Chip</v-chip>
                </v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action>
                <v-list-item-action-text v-text="item.action"></v-list-item-action-text>
                <v-btn icon v-if="!active" @click="saveOrEdit(index)">
                  <v-icon color="grey lighten-1">mdi-pencil</v-icon>
                </v-btn>
                <v-btn icon v-else @click="saveOrEdit(index)">
                  <v-icon color="blue">mdi-content-save-edit</v-icon>
                </v-btn>
              </v-list-item-action>
            </template>
          </v-list-item>

          <v-divider v-if="index + 1 < items.length" :key="index"></v-divider>
        </template>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    selected: undefined,
    items: [
      {
        action: "05/03/2020 10:30am",
        headline: "Brunch this weekend?",
        title: "Ali Connors",
        subtitle:
          "I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
      },
      {
        action: "2 hr",
        headline: "Summer BBQ",
        title: "me, Scrott, Jennifer",
        subtitle: "Wish I could come, but I'm out of town this weekend."
      },
      {
        action: "6 hr",
        headline: "Oui oui",
        title: "Sandra Adams",
        subtitle: "Do you have Paris recommendations? Have you ever been?"
      },
      {
        action: "12 hr",
        headline: "Birthday gift",
        title: "Trevor Hansen",
        subtitle:
          "Have any ideas about what we should get Heidi for her birthday?"
      },
      {
        action: "18hr",
        headline: "Recipe to try",
        title: "Britta Holt",
        subtitle:
          "We should eat this: Grate, Squash, Corn, and tomatillo Tacos."
      }
    ]
  }),
  methods: {
    saveOrEdit: function(index) {
      console.log(index);
      this.selected = undefined;
    },
    inEditMode: function(index) {
      return parseInt(this.selected) === index;
    }
  }
};
</script>
