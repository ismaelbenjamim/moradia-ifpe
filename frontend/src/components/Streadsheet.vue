<template>
  <div class="tasks_container">
    <div class="tasks_content">
      <h1>Tasks</h1>
      <ul class="tasks_list">
        <li v-for="task in tasks" :key="task.id">
          <h2>{{ task.campi.nome }}</h2>
          <p>{{ task.uuid }}</p>
          <button @click="toggleTask(task)">
            {{ task.completed ? 'Undo' : 'Complete' }}
          </button>
          <button @click="deleteTask(task)">Delete</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>/* eslint-disable */
export default {
  name: "Streadsheet",
  data() {
    return {
      // tasks
      tasks: ['']
    }
  },
  methods: {
    async getData() {
      try {
        // fetch tasks
        const response = await this.$http.get('http://localhost:8000/api/spreadsheet/');
        // set the data returned as tasks
        console.log(response.data)
        this.tasks = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
  },
  created() {
    // Fetch tasks on page load
    this.getData();
  }
}
</script>

<style scoped>

</style>
