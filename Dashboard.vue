<template>
  <div class="dashboard">
    <header class="dashboard-header">
      <h1>Social Media Dashboard</h1>
      <p>Powered by L8ab</p>
    </header>

    <div class="dashboard-content">
      <div class="stats-grid">
        <div class="stat-card">
          <h3>Total Posts</h3>
          <p class="stat-value">{{ stats.totalPosts }}</p>
        </div>
        <div class="stat-card">
          <h3>Engagement Rate</h3>
          <p class="stat-value">{{ stats.engagementRate }}%</p>
        </div>
        <div class="stat-card">
          <h3>Followers</h3>
          <p class="stat-value">{{ stats.followers }}</p>
        </div>
        <div class="stat-card">
          <h3>Reach</h3>
          <p class="stat-value">{{ stats.reach }}</p>
        </div>
      </div>

      <div class="posts-section">
        <h2>Recent Posts</h2>
        <div v-if="loading" class="loading">Loading posts...</div>
        <div v-else class="posts-list">
          <div v-for="post in posts" :key="post.id" class="post-card">
            <h4>{{ post.title }}</h4>
            <p>{{ post.content }}</p>
            <span class="post-date">{{ formatDate(post.created_at) }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'SocialMediaDashboard',
  setup() {
    const stats = ref({
      totalPosts: 0,
      engagementRate: 0,
      followers: 0,
      reach: 0
    });
    const posts = ref([]);
    const loading = ref(true);

    const fetchData = async () => {
      try {
        const [statsRes, postsRes] = await Promise.all([
          axios.get('/api/analytics/overview'),
          axios.get('/api/posts/')
        ]);
        stats.value = statsRes.data;
        posts.value = postsRes.data.results || [];
        loading.value = false;
      } catch (error) {
        console.error('Error fetching data:', error);
        loading.value = false;
      }
    };

    const formatDate = (date) => {
      return new Date(date).toLocaleDateString();
    };

    onMounted(() => {
      fetchData();
    });

    return {
      stats,
      posts,
      loading,
      formatDate
    };
  }
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 30px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

.stat-value {
  font-size: 2em;
  font-weight: bold;
  color: #4ECDC4;
}
</style>

