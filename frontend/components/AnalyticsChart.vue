<template>
  <div class="analytics-chart">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import Chart from 'chart.js/auto';

export default {
  name: 'AnalyticsChart',
  props: {
    data: {
      type: Object,
      required: true
    },
    type: {
      type: String,
      default: 'line'
    }
  },
  setup(props) {
    const chartCanvas = ref(null);
    let chartInstance = null;

    const createChart = () => {
      if (!chartCanvas.value) return;

      if (chartInstance) {
        chartInstance.destroy();
      }

      chartInstance = new Chart(chartCanvas.value, {
        type: props.type,
        data: props.data,
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Analytics Overview'
            }
          }
        }
      });
    };

    onMounted(() => {
      createChart();
    });

    watch(() => props.data, () => {
      createChart();
    }, { deep: true });

    return {
      chartCanvas
    };
  }
};
</script>
