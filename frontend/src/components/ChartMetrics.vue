<template>
  <div>
    <canvas ref="chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'

export default {
  name: 'ChartMetrics',
  props: [
    'labels',
    'mrrData',
    'chunrateData'
  ],
  data() {
    return {
      chart: null
    }
  },
  watch: {
    labels: {
      handler(newData) { this.renderChart(newData) },
      deep: true
    },
  },
  mounted() {
    this.renderChart()
  },
  methods: {
    renderChart() {
      const ctx = this.$refs.chart

      if (this.chart) {this.chart.destroy()}

      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.labels,
          datasets: [
            {
              label: 'MRR',
              data: this.mrrData,
            },

            {
              label: 'ChunRate',
              data: this.chunrateData,
              hidden: true
            }
          ]
        },
        options: {
          indexAxis: 'x',
        }
      })
    }
  }
}
</script>
