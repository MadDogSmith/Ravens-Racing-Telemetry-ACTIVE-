<script>
  import { onMount } from "svelte";
  import { io } from "socket.io-client";
  import * as echarts from "echarts";

  let chart;
  let timeData = [];
  let speedData = [];
  let rpmData = [];

  const socket = io("http://localhost:3001");

  onMount(() => {
    chart = echarts.init(document.getElementById("chart"));

    socket.on("telemetry", (data) => {
      timeData.push(new Date(data.time).toLocaleTimeString());
      speedData.push(data.speed);
      rpmData.push(data.rpm);

      // keep last 100 points
      if (timeData.length > 100) {
        timeData.shift();
        speedData.shift();
        rpmData.shift();
      }

      chart.setOption({
        title: { text: "🏎 Live Telemetry" },
        tooltip: { trigger: "axis" },
        xAxis: {
          type: "category",
          data: timeData
        },
        yAxis: { type: "value" },
        series: [
          {
            name: "Speed",
            type: "line",
            data: speedData
          },
          {
            name: "RPM",
            type: "line",
            data: rpmData
          }
        ]
      });
    });
  });
</script>

<style>
  body {
    background: #0f0f0f;
    color: white;
    font-family: Arial;
  }

  #chart {
    width: 100%;
    height: 500px;
  }
</style>

<h1>🏎 Svelte Telemetry Dashboard</h1>
<div id="chart"></div>