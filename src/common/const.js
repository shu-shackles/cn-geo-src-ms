const ASIDE_TITLE2 = [
    {
      title: "动态查询",
      titleIndex: "1",
      activeName: "1",
      icon: "el-icon-document",
      levelInfo: [
        {
          level: "矿物数据",
          levelIndex: "query_mineral",
          path: { name: "query_mineral" }
        },
        {
          level: "地质新闻",
          levelIndex: "query_news",
          path: { name: "query_news" }
        }
      ]
    },
    {
      title: "数据分析",
      titleIndex: "2",
      activeName: "2",
      icon: "el-icon-menu",
      levelInfo: [
        {
          level: "森林资源",
          levelIndex: "analysis_forest",
          path: { name: "analysis_forest" }
        },
        {
          level: "矿产资源",
          levelIndex: "analysis_mineral",
          path: { name: "analysis_mineral" }
        }
      ]
    }
  ];
const ASIDE_TITLE1 = [
  {
    title: "动态查询",
    titleIndex: "1",
    activeName: "1",
    icon: "el-icon-document",
    levelInfo: [
      {
        level: "矿物数据",
        levelIndex: "query_mineral",
        path: { name: "query_mineral" }
      },
      {
        level: "地质新闻",
        levelIndex: "query_news",
        path: { name: "query_news" }
      }
    ]
  },
  {
    title: "数据分析",
    titleIndex: "2",
    activeName: "2",
    icon: "el-icon-menu",
    levelInfo: [
      {
        level: "森林资源",
        levelIndex: "analysis_forest",
        path: { name: "analysis_forest" }
      },
      {
        level: "矿产资源",
        levelIndex: "analysis_mineral",
        path: { name: "analysis_mineral" }
      }
    ]
  },
  {
    title: "系统管理",
    titleIndex: "3",
    activeName: "3",
    icon: "el-icon-setting",
    levelInfo: [
      {
        level: "数据审核",
        levelIndex: "data_audit",
        path: { name: "data_audit" }
      }
    ]
  }
];
const ASIDE_TITLE0 = [
  {
    title: "动态查询",
    titleIndex: "1",
    activeName: "1",
    icon: "el-icon-document",
    levelInfo: [
      {
        level: "矿物数据",
        levelIndex: "query_mineral",
        path: { name: "query_mineral" }
      },
      {
        level: "地质新闻",
        levelIndex: "query_news",
        path: { name: "query_news" }
      }
    ]
  },
  {
    title: "数据分析",
    titleIndex: "2",
    activeName: "2",
    icon: "el-icon-menu",
    levelInfo: [
      {
        level: "森林资源",
        levelIndex: "analysis_forest",
        path: { name: "analysis_forest" }
      },
      {
        level: "矿产资源",
        levelIndex: "analysis_mineral",
        path: { name: "analysis_mineral" }
      }
    ]
  },
  {
    title: "系统管理",
    titleIndex: "3",
    activeName: "3",
    icon: "el-icon-setting",
    levelInfo: [
      {
        level: "数据审核",
        levelIndex: "data_audit",
        path: { name: "data_audit" }
      },
      {
        level: "用户管理",
        levelIndex: "setting_user",
        path: { name: "setting_user" }
      }
    ]
  }
];

const Project = [
  {
    label: "巫山三峡",
    value: 1
  },
  {
    label: "延长",
    value: 2
  }
];

const TableType = [
  {
    label: "煤炭",
    unit: "亿吨",
    query: "coal(100M tons)",
    value: 0
  },
  {
    label: "石油",
    unit: "万吨",
    query: "fossil_oil(10K tons)",
    value: 1
  },
  {
    label: "天然气",
    unit: "亿立方米",
    query: "gas(100M cubic meters)",
    value: 2
  },
  {
    label: "铁矿",
    unit: "亿吨",
    query: "iron(100M tons)",
    value: 3
  },
  {
    label: "铜矿",
    unit: "万吨",
    query: "bronze(10K tons)",
    value: 4
  },
  {
    label: "铅矿",
    unit: "万吨",
    query: "lead(10k tons)",
    value: 5
  },
  {
    label: "锌矿",
    unit: "万吨",
    query: "zinc(10k tons)",
    value: 6
  },
  {
    label: "金矿",
    unit: "吨",
    query: "gold(tons)",
    value: 7
  },
  {
    label: "银矿",
    unit: "吨",
    query: "silver(tons)",
    value: 8
  },
  {
    label: "硫铁矿",
    unit: "万吨",
    query: "FeS2(10k tons)",
    value: 9
  }
];

const ForestType = [
  {
    label: "森林覆盖面积",
    value: 0
  },
  {
    label: "自然林面积",
    value: 1
  },
  {
    label: "人工林面积",
    value: 2
  }
];

const Points = [
  {
    label: "GPS点",
    value: 1,
    children: [
      {
        label: "x1",
        value: 11
      },
      {
        label: "x2",
        value: 12
      }
    ]
  },
  {
    label: "地表监测点",
    value: 2,
    children: [
      {
        label: "x1",
        value: 21
      },
      {
        label: "x2",
        value: 22
      }
    ]
  },
  {
    label: "深部监测点",
    value: 3,
    children: [
      {
        label: "全部",
        value: 30
      },
      {
        label: "SW01",
        value: 31
      },
      {
        label: "SW02",
        value: 32
      },
      {
        label: "SW03",
        value: 31
      },
      {
        label: "SW04",
        value: 32
      },
      {
        label: "SW05",
        value: 31
      },
      {
        label: "SW06",
        value: 32
      },
      {
        label: "SW07",
        value: 31
      },
      {
        label: "SW08",
        value: 32
      },
      {
        label: "SW09",
        value: 31
      },
      {
        label: "SW10",
        value: 32
      },
      {
        label: "SW11",
        value: 31
      },
      {
        label: "SW12",
        value: 32
      }
    ]
  }
];

const headerConfig = [
  {
    name: "survey",
    headerShow: [false, true, false, false, false],
    // 时间，项目，表的类型（温度，降水），监测点
    contrast: false
  },
  {
    name: "word",
    headerShow: [false, true, false, false, false, true],
    contrast: false
  },

  {
    name: "graph",
    headerShow: [false, true, false, false, false, true],
    contrast: false
  },
  {
    name: "img",
    headerShow: [false, true, false, false, true, true],
    contrast: false
  },
  {
    name: "mineralData",
    headerShow: [true, false, false, true, false, true, true, true],
    contrast: false
  },
  {
    name: "geoNews",
    headerShow: [false, true, false, true, false],
    contrast: true
  },
  {
    name: "ForestAnalysis",
    headerShow: [false, false, true, true, false],
    contrast: false
  },
  {
    name: "MineralAnalysis",
    headerShow: [true, false, false, false, false],
    contrast: false
  }
];

const pageConfig = [
  {
    name: "one",
    oneChart: "HighChart"
  },
  {
    name: "two",
    oneChart: "TwoCharts"
  }
];

let getHeaderConfig = name => {
  let b = {};
  headerConfig.forEach(item => {
    if (item.name === name) {
      b = item;
    }
  });
  return b;
};

let getPageConfig = name => {
  let b = {};
  pageConfig.forEach(item => {
    if (item.name === name) {
      b = item;
    }
  });
  return b;
};
export {
  ASIDE_TITLE0,
  ASIDE_TITLE1,
  ASIDE_TITLE2,
  Project,
  Points,
  TableType,
  ForestType,
  getHeaderConfig,
  getPageConfig
};
