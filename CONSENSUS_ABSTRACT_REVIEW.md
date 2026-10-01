# Consensus MCP 摘要精读记录（104 篇）

更新日期：2026-10-01

## 范围与读取状态

本记录覆盖当前纳入书目的 104 篇（初筛标记：核心 30 篇、相邻/背景 74 篇）。Consensus MCP 按 DOI 检索并调用 `fetch` 后，104 篇均与本地 DOI 精确匹配，且取得摘要文本。5 条 `fetch` 记录只返回题录与 takeaway，另以同 DOI 的 Consensus 搜索记录补齐摘要；其余摘要直接由 `fetch` 返回。

**证据边界：** 当前 Consensus MCP 的 `fetch` 提供题录、摘要和 takeaway，不提供论文正文。下面每篇的概述、主题判断和核查点均基于摘要，不是全文阅读结论。全库既有全文状态仍为：26 篇已完成全文阅读，5 篇全文不可取得，73 篇尚未开始全文阅读。尤其不能仅凭摘要把方法描述、实验或理论保证升级为全文核验结论。

全文核读优先级应先给直接处理解支延续/转换、奇异跨越和路径级关节约束的研究；纯单点解析 IK、一般路径规划或跨机器人类别综述可放在背景层。

## 跨文献归纳（摘要证据）

1. **解支一致性不是单一问题。** 摘要中出现连续伪逆、重复/周期 IK、冗余参数化、候选解图连接、有限状态选择、学习式多解集合预测等路线。候选图与逐点选解能连接离散候选，但是否保证同一连续可微解支，需要核对节点/边定义及采样间隙。
2. **奇异性回避与奇异性转换必须分开。** 多数方法通过阻尼、势场、可操作度或最小奇异值阈值避开奇异区。少数研究直接处理跨奇异换支；cuspidal 机构还可能在不穿越奇异的情况下换解。三种情况的可行条件并不相同。
3. **约束层次从静态限位到动态可行性。** 文献摘要涉及关节位置、速度、加速度、jerk、力矩/功率、碰撞距离、RCM、Cartesian 误差管以及全身碰撞。QP/LP、viability、NMPC 和离散动态规划提供不同层级的约束处理；离散/采样可行性不自动等于连续时间保证。
4. **实验强度差异明显。** 有些研究报告实机或硬件控制器，有些仅有仿真、数值例或优化器基准。需要全文核对机器人几何、轨迹范围、奇异类型、采样/离散误差、基线、公平性和运行指标。
5. **候选综述的证据分工。** 解析 IK 与 SEW/arm-angle 参数化解释解支如何产生；路径图、continuation、周期性及连续性选择处理跨帧关联；QP/LP/NMPC 和轨迹优化处理运动约束；奇异分类文献决定“回避、穿越、无奇异换支”应如何分层论述。

## 核心候选摘要卡（30 篇）

### 001. [A Fast Evaluation of Initial Configurations in Repeatable Inverse Kinematics for Redundant Manipulators](https://consensus.app/papers/a-fast-evaluation-of-initial-configurations-in-repeatable-dulęba-karcz-dulęba/6cde4e7c308e509ab7dbca292c1068e7/?utm_source=chatgpt)

- **书目信息：** Dulęba, I.; Karcz-Dulęba, I.; Mielczarek, Arkadiusz（2018），International Journal of Applied Mathematics and Computer Science；[DOI](https://doi.org/10.2478/amcs-2018-0037)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.2478/amcs-2018-0037`。
- **摘要精读：** 针对冗余机械臂的重复逆运动学闭环任务，放开固定入口姿态，提出用 manipulability 子椭球特征快速筛选/优化能生成短关节轨迹的初始构型。
- **与主题的关系：** 直接涉及周期轨迹的起始分支/构型选择，可作为轨迹一致性前置条件；不是沿轨迹在线跟踪算法。
- **全文待核：** 摘要没有给出机器人、约束、连续性证明或实验量化细节。

### 002. [A Novel Approach for a Inverse Kinematics Solution of a Redundant Manipulator](https://consensus.app/papers/a-novel-approach-for-a-inverse-kinematics-solution-of-a-kelemen-virgala/05a67a701b2b5f54b02a23f84d396860/?utm_source=chatgpt)

- **书目信息：** Kelemen, M.; Virgala, Ivan; Lipták, T.; Miková, L.; Filakovský, Filip; Bulej, V.（2018），Applied Sciences；[DOI](https://doi.org/10.3390/app8112229)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/app8112229`。
- **摘要精读：** 用加权 Jacobian 控制冗余度，把关节限位、奇异性回避、障碍回避列为次任务，并用势场规划末端从起点到目标的路径；仿真报告计算时间下降。
- **与主题的关系：** 涉及路径执行中的约束优先级和奇异性回避。
- **全文待核：** 摘要未证明分支连续或硬约束可行；奇异点被回避而非跨越，证据为仿真。

### 003. [Global Redundancy Resolution via Continuous Pseudoinversion of the Forward Kinematic Map](https://consensus.app/papers/global-redundancy-resolution-via-continuous-hauser-emmons/2cb33d21b5b453e6bb3a9a5ed6d10f8c/?utm_source=chatgpt)

- **书目信息：** Hauser, Kris; Emmons, Scott（2018），IEEE Transactions on Automation Science and Engineering；[DOI](https://doi.org/10.1109/tase.2018.2805878)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tase.2018.2805878`。
- **摘要精读：** 把冗余解析写成正向运动学的连续伪逆，使同一工作空间点对应同一关节姿态；采样工作空间/关节空间路线并以 Max-SAT 减少不连续边界。
- **与主题的关系：** 重要的全局分支一致性框架，可服务于路径跟踪与工作空间设计。
- **全文待核：** 摘要明确是最小化而非消除不连续；演示和约束边界、奇异转换细节需全文核查。

### 004. [On Higher Order Inverse Kinematics Methods in Time-Optimal Trajectory Planning for Kinematically Redundant Manipulators](https://consensus.app/papers/on-higher-order-inverse-kinematics-methods-in-timeoptimal-reiter-mueller/13201c3886315896916d07c6cf20514f/?utm_source=chatgpt)

- **书目信息：** Reiter, Alexander; Mueller, Andreas; Gattringer, H.（2018），IEEE Transactions on Industrial Informatics；[DOI](https://doi.org/10.1109/tii.2018.2792002)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tii.2018.2792002`。
- **摘要精读：** 为预定义末端路径上的时间最优跟随推导高阶逆运动学，以关节空间分解和高阶伪逆解析冗余；两类机械臂示例并做实验验证。
- **与主题的关系：** 核心：把高阶 IK、连续可执行性、时间最优和工艺约束连起来。
- **全文待核：** 摘要未揭示分支标识、奇异过渡条件及约束的数学保证。

### 005. [Analytical Inverse Kinematics and Self-Motion Application for 7-DOF Redundant Manipulator](https://consensus.app/papers/analytical-inverse-kinematics-and-selfmotion-gong-li/6cfad33bb0c8521f98dc097e5e12ec1e/?utm_source=chatgpt)

- **书目信息：** Gong, Ming-De; Li, Xiangdong; Zhang, Lei（2019），IEEE Access；[DOI](https://doi.org/10.1109/access.2019.2895741)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/access.2019.2895741`。
- **摘要精读：** 针对 7 自由度机械臂用肘角参数化多解，沿连续末端路径从离散 IK 解中构造连续关节向量；通过肘角区间、限位/碰撞子空间交集筛出可行解。
- **与主题的关系：** 核心：显式处理多解连续选择、关节限位与避障。
- **全文待核：** 摘要所述验证为运动学仿真；分支连续定义、全路径保证和奇异处理未明确。

### 008. [Inverse Kinematics with Forward Dynamics Solvers for Sampled Motion Tracking](https://consensus.app/papers/inverse-kinematics-with-forward-dynamics-solvers-for-scherzinger-roennau/f42fb2531286587286884dcf25e5d6a8/?utm_source=chatgpt)

- **书目信息：** Scherzinger, Stefanie; Roennau, A.; Dillmann, R.（2019），2019 19th International Conference on Advanced Robotics (ICAR)；[DOI](https://doi.org/10.1109/icar46387.2019.8981554)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/icar46387.2019.8981554`。
- **摘要精读：** 面向未知先验的离散采样 Cartesian 目标，改造 Jacobian transpose IK：用虚拟条件化机械臂的质量矩阵增强控制；UR10 结果报告优于普通 Jacobian 法。
- **与主题的关系：** 补充在线采样跟踪控制背景。
- **全文待核：** 抽象层只说连续执行需要平滑状态过渡，未给出分支连续或关节约束保证；评价范围看起来限于 UR10。

### 013. [Globally Optimal Inverse Kinematics Method for a Redundant Robot Manipulator with Linear and Nonlinear Constraints](https://consensus.app/papers/globally-optimal-inverse-kinematics-method-for-a-tringali-cocuzza/4189f6deb8585166852a1ed6b3189cf6/?utm_source=chatgpt)

- **书目信息：** Tringali, A.; Cocuzza, S.（2020），Robotics；[DOI](https://doi.org/10.3390/robotics9030061)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/robotics9030061`。
- **摘要精读：** 冗余机械臂轨迹 IK 以满足运动学约束的初始关节轨迹启动多起点优化，可优化能量/力矩等积分代价，支持多目标、周期轨迹及位置/速度/力矩/功率约束。
- **与主题的关系：** 强相关的轨迹级约束优化，并涵盖周期路径。
- **全文待核：** 摘要把方法称为全局最优，但描述多起点算法；全局保证、离散化与分支连续细节须全文核实；展示为 3-DOF 仿真。

### 016. [Inverse Kinematics of Redundant Manipulators With Dynamic Bounds on Joint Movements](https://consensus.app/papers/inverse-kinematics-of-redundant-manipulators-with-faroni-beschi/7b5baf76c9315f2ab1fd16003d5fe313/?utm_source=chatgpt)

- **书目信息：** Faroni, M.; Beschi, M.; Pedrocchi, N.（2020），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2020.3013879)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2020.3013879`。
- **摘要精读：** 为冗余臂加入动态关节运动边界，限制求解结果相对一条无碰撞名义关节轨迹的偏移量；用线性约束和次任务权重自动调节，含数值与实验结果。
- **与主题的关系：** 轨迹级关节运动约束及受限偏移，具直接工程相关性。
- **全文待核：** 保证依赖给定无碰撞参考轨迹；摘要未说明分支标签、跨奇异性或全局连续保证。

### 017. [A Modified DLS Scheme With Controlled Cyclic Solution for Inverse Kinematics in Redundant Robots](https://consensus.app/papers/a-modified-dls-scheme-with-controlled-cyclic-solution-for-safeea-béarée/fddf6cbb13875e24874ead0e9372afe7/?utm_source=chatgpt)

- **书目信息：** Safeea, Mohammad; Béarée, Richard; Neto, P.（2021），IEEE Transactions on Industrial Informatics；[DOI](https://doi.org/10.1109/tii.2021.3060019)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tii.2021.3060019`。
- **摘要精读：** 针对 DLS 的非周期性提出受控循环解，使末端闭合 Cartesian 回路对应闭合关节回路；在 9-DOF 仿真及 7-DOF 实机测试。
- **与主题的关系：** 直接解决重复轨迹的关节空间重复性，是轨迹一致性核心候选。
- **全文待核：** 摘要未披露算法构造、约束细节和奇异转换行为。

### 026. [Modified Configuration Control With Potential Field for Inverse Kinematic Solution of Redundant Manipulator](https://consensus.app/papers/modified-configuration-control-with-potential-field-for-kim-wang/d935dcc62fdd5cc88fe2e3f09fcde1aa/?utm_source=chatgpt)

- **书目信息：** Kim, Jaehyung; Wang, Jie; Kim, Hyun-Hee; Lee, Min Choel（2021），IEEE/ASME Transactions on Mechatronics；[DOI](https://doi.org/10.1109/tmech.2021.3077914)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tmech.2021.3077914`。
- **摘要精读：** 用势场调节冗余臂角速度配置以跟踪末端方向，同时避开关节角限位和障碍；仿真报告更快，7-DOF 实验验证可实时回避。
- **与主题的关系：** 在线冗余控制中把末端任务与限位/障碍结合。
- **全文待核：** 摘要未给出连续分支或奇异转换的保证；传统 SVD 奇异处理仍是背景问题。

### 027. [Multi-Objective Swarm Intelligence Trajectory Generation for a 7 Degree of Freedom Robotic Manipulator](https://consensus.app/papers/multiobjective-swarm-intelligence-trajectory-malik-henderson/3ac7670adbd957e4b8e2afd89b7a70d9/?utm_source=chatgpt)

- **书目信息：** Malik, Aryslan; Henderson, T.; Prazenica, Richard（2021），Robotics；[DOI](https://doi.org/10.3390/robotics10040127)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/robotics10040127`。
- **摘要精读：** 用群智能与 PoE 生成 7-DOF 关节轨迹，满足末端有限 jerk、避障并降控制努力；与 IK/PSO 比较并在 Sawyer 上试验。
- **与主题的关系：** 强轨迹级证据，联合运动平滑、避障和控制代价。
- **全文待核：** 摘要没有明确分支追踪或硬关节位置/速度/加速度限值，也未报告奇异转换。

### 030. [Singularity Configuration Pass Algorithm of Manipulator Based on PVT Trajectory Planning](https://consensus.app/papers/singularity-configuration-pass-algorithm-of-manipulator-he-liu/9aea8d7f9afc5173b33f632be5f0bbeb/?utm_source=chatgpt)

- **书目信息：** He, Chunlai; Liu, Yunfei; Cheng, Shuo（2021），2021 6th International Conference on Control, Robotics and Cybernetics (CRC)；[DOI](https://doi.org/10.1109/crc52766.2021.9620142)。
- **初筛 / 全文状态：** 核心 / `PAYWALLED_OR_UNAVAILABLE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/crc52766.2021.9620142`。
- **摘要精读：** 用解析 IK 识别三类奇异构型，并结合 PVT 轨迹规划设计通过算法，声称经过奇异时保持运动连续和稳定；含理论及仿真/实验数据分析。
- **与主题的关系：** 直接针对奇异配置穿越时的轨迹连续性，核心候选。
- **全文待核：** 摘要不提供算法细节、连续阶数、机器人实例和约束证明；需全文辨别所谓实验数据的证据性质。

### 031. [A Dynamic Programming Framework for Optimal Planning of Redundant Robots Along Prescribed Paths With Kineto-Dynamic Constraints](https://consensus.app/papers/a-dynamic-programming-framework-for-optimal-planning-of-ferrentino-savino/f5413f79d1195cb6915cf33ad9fb6dd9/?utm_source=chatgpt)

- **书目信息：** Ferrentino, Enrico; Savino, H.; Franchi, A.; Chiacchio, P.（2024），IEEE Transactions on Automation Science and Engineering；[DOI](https://doi.org/10.1109/tase.2023.3330371)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tase.2023.3330371`。
- **摘要精读：** 把冗余臂预设路径 IK 与时间参数化合并为离散动态规划，在给定离散分辨率下保证全局最优；Panda 实机规划执行，纳入平滑和执行器饱和实践。
- **与主题的关系：** 强轨迹级 kineto-dynamic 优化，联合约束与真实执行。
- **全文待核：** 全局最优只对离散网格成立；摘要称需小时级规划，非频繁重规划；对分支连续需全文看 DP 状态/边定义。

### 032. [A novel QP-based kinematic redundancy resolution method with joint constraints satisfaction](https://consensus.app/papers/a-novel-qpbased-kinematic-redundancy-resolution-method-wolinski-wojtyra/fc697a581f0d5e448d31fa91ac33ba76/?utm_source=chatgpt)

- **书目信息：** Wolinski, Lukasz; Wojtyra, M.（2022），IEEE Access；[DOI](https://doi.org/10.1109/access.2022.3167403)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/access.2022.3167403`。
- **摘要精读：** 加速度作为 QP 决策量，用离散关节状态方程同时施加位置、速度、加速度约束；KUKA LWR4+ 7-DOF 数值测试对比伪逆。
- **与主题的关系：** 直接覆盖位置/速度/加速度约束的微分冗余 IK。
- **全文待核：** 摘要报告数值研究；连续解支、奇异过渡、硬约束闭环鲁棒性未验证。

### 036. [An Inverse Kinematic Optimization Method for the S-R-S Redundant Manipulator Considering Joint Limit and Singular Position Avoidance](https://consensus.app/papers/an-inverse-kinematic-optimization-method-for-the-srs-mei-chen/ac18503f4a8b5a6e8ee91b4a6b0e48f3/?utm_source=chatgpt)

- **书目信息：** Mei, Yisheng; Chen, Xin（2022），2022 41st Chinese Control Conference (CCC)；[DOI](https://doi.org/10.23919/ccc55666.2022.9902201)。
- **初筛 / 全文状态：** 核心 / `PAYWALLED_OR_UNAVAILABLE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.23919/ccc55666.2022.9902201`。
- **摘要精读：** 利用 S-R-S 几何以臂角参数化解支，先求包含奇异/非奇异情形的可行臂角范围，再以虚拟力代价和二次近似同时避开关节限位和奇异位置；仿真比较。
- **与主题的关系：** 直接针对连续轨迹中的冗余分支参数、限位与奇异回避。
- **全文待核：** 摘要未给路径连续性/可行性证明或实机验证；主要适用 S-R-S 结构。

### 037. [Evolutionary multi-objective trajectory optimization for a redundant robot in Cartesian space considering obstacle avoidance](https://consensus.app/papers/evolutionary-multiobjective-trajectory-optimization-liu-li/c4b74374adb5509ca333ba7890f2c10d/?utm_source=chatgpt)

- **书目信息：** Liu, Yong; Li, Xiang; Jiang, Pei-Yang; Du, Z.; Wu, Zhe; Sun, Boxi; Huang, Xin-Yan（2022），Mechanical Sciences；[DOI](https://doi.org/10.5194/ms-13-41-2022)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.5194/ms-13-41-2022`。
- **摘要精读：** 以余弦多项式生成 Cartesian 轨迹，零空间处理限位，实时碰撞检测，再用多目标 PSO 同时优化障碍距离、关节速度、jerk 与能耗；仿真结果报告平滑且满足限制。
- **与主题的关系：** 轨迹级多约束与多目标优化的直接候选。
- **全文待核：** 证据为仿真；“满足限制”的约束实现和分支跳变/奇异跨越需全文确认。

### 045. [Singularity Avoidance with Application to Online Trajectory Optimization for Serial Manipulators](https://consensus.app/papers/singularity-avoidance-with-application-to-online-beck-vu/5314c2268d8752dca126e365d3b3fe73/?utm_source=chatgpt)

- **书目信息：** Beck, F.; Vu, Minh; Hartl-Nesic, C.; Kugi, A.（2023），IFAC-PapersOnLine；[DOI](https://doi.org/10.1016/j.ifacol.2023.10.1582)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus search result（已另行 fetch 核实题录）；Consensus DOI 匹配：`10.1016/j.ifacol.2023.10.1582`。
- **摘要精读：** 基于三种串联臂的已知奇异构型设计定制势函数，实时轨迹优化中与可操作度最大化做 Monte Carlo 比较，报告更短/更快轨迹。
- **与主题的关系：** 利用机器人结构奇异集合改善在线路径优化。
- **全文待核：** 仍是奇异回避；摘要未涉及分支身份或硬关节约束。

### 046. [A comparison of methods solving repeatable inverse kinematics for robot manipulators](https://consensus.app/papers/a-comparison-of-methods-solving-repeatable-inverse-dulęba-karcz-dulęba/c3b9e7b4ddd5510e8d6cc80734dd3ba9/?utm_source=chatgpt)

- **书目信息：** Dulęba, I.; Karcz-Dulęba, I.（2018），Archives of Control Sciences；[DOI](https://doi.org/10.24425/119074)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.24425/119074`。
- **摘要精读：** 比较两类重复 IK 方法：continuation 与连续近似，基于多路径、多初始构型和不同冗余度的摆杆机器人仿真，做定量/定性评估。
- **与主题的关系：** 核心方法对照，帮助辨析路径延续策略的质量。
- **全文待核：** 样机为摆杆仿真；摘要未给统计结果或工业臂、奇异跨越约束。

### 048. [A Research on Manipulator-Path Tracking Based on Deep Reinforcement Learning](https://consensus.app/papers/a-research-on-manipulatorpath-tracking-based-on-deep-zhang-zhang/dd94fbcd410d54f4815b45c25ae2cc02/?utm_source=chatgpt)

- **书目信息：** Zhang, P.; Zhang, Jie; Kan, J.（2023），Applied Sciences；[DOI](https://doi.org/10.3390/app13137867)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/app13137867`。
- **摘要精读：** 把机械臂连续路径跟踪建成最大熵深度强化学习序贯决策，端到端控制以避免逐离散位姿调用不一致的 IK；报告连续空间实验。
- **与主题的关系：** 与 IK 路径不一致问题相邻，可作为替代控制路线。
- **全文待核：** 刻意不求 IK，故不是分支追踪方案；约束保证与泛化细节未给。

### 053. [Constrained-Differential-Kinematics-Decomposition-Based NMPC for Online Manipulator Control with Low Computational Costs](https://consensus.app/papers/constraineddifferentialkinematicsdecompositionbased-reinhold-baumann/a39f63a196b55779b5c261a84eadf18f/?utm_source=chatgpt)

- **书目信息：** Reinhold, Jan; Baumann, H.; Meurer, T.（2023），Robotics；[DOI](https://doi.org/10.3390/robotics12010007)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/robotics12010007`。
- **摘要精读：** 分解微分运动学以构造低成本全约束 NMPC，联合关节/Cartesian 约束和障碍安全距离跟踪；Stäubli TX2-90 Gazebo 仿真。
- **与主题的关系：** 在线受约束轨迹控制与避障背景。
- **全文待核：** 证据为仿真；没有解支状态或奇异转换机制。

### 056. [Generation of Configuration Space Trajectories Over Semi-Constrained Cartesian Paths for Robotic Manipulators](https://consensus.app/papers/generation-of-configuration-space-trajectories-over-malhan-thakar/a9c9019964a457c1a1916c17abcddad9/?utm_source=chatgpt)

- **书目信息：** Malhan, R.; Thakar, Shantanu; Kabir, A.; Rajendran, Pradeep; Bhatt, P.; Gupta, Satyandra（2023），IEEE Transactions on Automation Science and Engineering；[DOI](https://doi.org/10.1109/tase.2022.3144673)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tase.2022.3144673`。
- **摘要精读：** 为半约束 Cartesian 路径和多 TCP 设计迭代图搜索：节点包含多个 IK 候选，再按任务空间质量连接成轨迹，工业测试报告更少图边且近优。
- **与主题的关系：** 核心：显式把多解候选组织成路径图并考虑末端容差/多接触点。
- **全文待核：** 摘要未给分支连续/奇异通过约束证明、评价细节及具体机器人配置。

### 062. [Mathematical modeling and simulation of the inverse kinematic of a redundant robotic manipulator using azimuthal angles and spherical polar piecewise interpolation](https://consensus.app/papers/mathematical-modeling-and-simulation-of-the-inverse-dupac/7bb81d01e70f54ab9726e1f223e96b0e/?utm_source=chatgpt)

- **书目信息：** Dupac, Mihai（2023），Math. Comput. Simul.；[DOI](https://doi.org/10.1016/j.matcom.2023.02.010)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus search result（已另行 fetch 核实题录）；Consensus DOI 匹配：`10.1016/j.matcom.2023.02.010`。
- **摘要精读：** 在球坐标中用五次 Hermite 分段插值构造平滑末端路径，再建冗余臂 IK/动力学并优化关节速度、误差、时间、能量或功率；Matlab 数值例。
- **与主题的关系：** Cartesian 路径构造与多性能量纲耦合的轨迹优化背景。
- **全文待核：** 摘要没有解支一致性、关节约束或实机试验信息。

### 067. [Time-Optimal Asymmetric S-Curve Trajectory Planning of Redundant Manipulators under Kinematic Constraints](https://consensus.app/papers/timeoptimal-asymmetric-scurve-trajectory-planning-of-liu-cui/ac67dc97866d5bb5a0e88706dc7946d6/?utm_source=chatgpt)

- **书目信息：** Liu, Tianyu; Cui, Jingkai; Li, Yanhui; Gao, Si-Yuan; Zhu, Mingchao; Chen, Liheng（2023），Sensors (Basel, Switzerland)；[DOI](https://doi.org/10.3390/s23063074)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/s23063074`。
- **摘要精读：** WOA 调整冗余臂的不对称 S 曲线速度时序，将关节运动学限制换算为末端路径段限制，并生成 jerk 受限、时间优化轨迹；有模拟和实机实验。
- **与主题的关系：** 关节运动约束与时间参数化的轨迹证据。
- **全文待核：** 轨迹 IK 分支选择/奇异通过机制未述；全局最优性及 WOA 停止准则需全文核实。

### 071. [BoundMPC: Cartesian path following with error bounds based on model predictive control in the joint space](https://consensus.app/papers/boundmpc-cartesian-path-following-with-error-bounds-based-oelerich-beck/36597eb672755110ae2cbcfa8805a44d/?utm_source=chatgpt)

- **书目信息：** Oelerich, Thies; Beck, F.; Hartl-Nesic, Christian; Kugi, Andreas（2024），The International Journal of Robotics Research；[DOI](https://doi.org/10.1177/02783649241309354)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1177/02783649241309354`。
- **摘要精读：** BoundMPC 在关节空间用模型预测控制跟踪带误差界的 Cartesian 路径，误差管道编码避障和任务限制，可在运行中重规划；iiwa 五类实机场景。
- **与主题的关系：** 在线路径跟踪、误差界和全身碰撞/任务约束的强实验证据。
- **全文待核：** 允许有界偏离参考路径，摘要未显式证明 IK 解支连续或奇异转换。

### 075. [IKLink: End-Effector Trajectory Tracking with Minimal Reconfigurations](https://consensus.app/papers/iklink-endeffector-trajectory-tracking-with-minimal-wang-sifferman/84297aa7d6a253abb3e2fa1390d7dcd3/?utm_source=chatgpt)

- **书目信息：** Wang, Yeping; Sifferman, Carter; Gleicher, M.（2024），2024 IEEE International Conference on Robotics and Automation (ICRA)；[DOI](https://doi.org/10.1109/icra57147.2024.10611510)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/icra57147.2024.10611510`。
- **摘要精读：** IKLink 为路径每个 waypoint 生成多样 IK 候选，再用图和 DP 链接以最少重构跟踪末端轨迹，含模拟和实体机器人展示。
- **与主题的关系：** 核心：候选图搜索与跨路径解选择。
- **全文待核：** 方法明确容许发生 reconfiguration break 并重置构型，因此不保证一条不中断分支；需计入任务时间/能耗代价。

### 076. [Kinematic issues in 6R cuspidal robots, guidelines for path planning and deciding cuspidality](https://consensus.app/papers/kinematic-issues-in-6r-cuspidal-robots-guidelines-for-path-salunkhe-marauli/05c87ca85bcf55ad9fba065037fdf7bb/?utm_source=chatgpt)

- **书目信息：** Salunkhe, Durgesh Haribhau; Marauli, Tobias; Müller, A.; Chablat, D.; Wenger, P.（2024），The International Journal of Robotics Research；[DOI](https://doi.org/10.1177/02783649241293481)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1177/02783649241293481`。
- **摘要精读：** 讨论 6R cuspidal 臂可在不穿越奇异性的条件下换 IK 解，系统分析初始分支对给定路径可行与重复性的影响，并提出 cuspidality 判别和路径测试流程。
- **与主题的关系：** 奇异与非奇异分支转换机制的关键综述/方法背景。
- **全文待核：** 适用 cuspidal 6R；CUSPIDAL 非奇异换支不可泛化到必须跨奇异的 non-cuspidal 机构。

### 078. [Optimizing Redundant Robot Kinematics and Motion Planning via Advanced D-H Analysis and Enhanced Artificial Potential Fields](https://consensus.app/papers/optimizing-redundant-robot-kinematics-and-motion-zhang-chen/ac5bd04573a950079942fc6ab44f5962/?utm_source=chatgpt)

- **书目信息：** Zhang, Xuanming; Chen, Lei; Dong, Weian; Li, Chunxu（2024），Electronics；[DOI](https://doi.org/10.3390/electronics13163304)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/electronics13163304`。
- **摘要精读：** DH 求冗余臂八组向量解，以 IK 误差和关节运动平滑为目标选解，再结合改进势场与 RRT 避障；MATLAB/CoppeliaSim 联合仿真。
- **与主题的关系：** 多解候选、平滑代价与路径规划的组合背景。
- **全文待核：** 主要仿真且摘要未报告分支连续/硬限位证明；质量和泛化需全文评估。

### 094. [A Multi-Objective Hybrid PSO-DLS Optimization Framework for Redundant Inverse Kinematics of Anthropomorphic Upper-Limb Manipulators](https://consensus.app/papers/a-multiobjective-hybrid-psodls-optimization-framework-xu-li/fee60b6460d059e48e1409235a904269/?utm_source=chatgpt)

- **书目信息：** Xu, Dong; Li, Yi-Bin; Xu, Han; Zhang, Xu; Ju, Jinyong; Zhou, Qi-Cai; Ren, Yi-Jie（2026），International Journal of Humanoid Robotics；[DOI](https://doi.org/10.1142/s0219843626500064)。
- **初筛 / 全文状态：** 核心 / `PAYWALLED_OR_UNAVAILABLE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1142/s0219843626500064`。
- **摘要精读：** 2026 混合 DLS 与按帧难度触发的 PSO，以位姿误差、manipulability 与帧间关节变化统一代价，配以前帧热启动、早停与关节投影；有基线、消融、敏感性。
- **与主题的关系：** 高度核心：直接处理冗余 IK 的帧间不连续及奇异/限位风险。
- **全文待核：** 证据仍仅摘要；“投影/保持可行”不等同全路径硬位置/速度/加速度保证，机器人/数据指标待全文核查。

### 096. [Ensuring Viability: A QP-based Inverse Kinematics for Handling Joint Range, Velocity and Acceleration Limits, as Well as Whole-body Collision Avoidance](https://consensus.app/papers/ensuring-viability-a-qpbased-inverse-kinematics-for-zhang-kikuuwe/ca02db575e615cc58e19c604d21e3c96/?utm_source=chatgpt)

- **书目信息：** Zhang, Yachen; Kikuuwe, Ryo（2026），Journal of Intelligent & Robotic Systems；[DOI](https://doi.org/10.1007/s10846-025-02335-z)。
- **初筛 / 全文状态：** 核心 / `READ_COMPLETE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1007/s10846-025-02335-z`。
- **摘要精读：** 两阶段 QP IK 在离线计算可行状态参数、在线实时更新线性约束，同时处理关节位置/速度/加速度与全身碰撞；附加约束旨在保证状态可行，摘要仅报仿真。
- **与主题的关系：** 核心约束可行性方法，提供位置/速度/加速度与碰撞联合处理。
- **全文待核：** 没有解支连续或奇异跨越分析；可行性保证假设与实验验证需全文检查。

### 097. [Handling Transitions Across Singularities for UR-Like Serial Robots](https://consensus.app/papers/handling-transitions-across-singularities-for-urlike-boschi-toni/8c5bd288ea885f74bdc311f03afc8a2b/?utm_source=chatgpt)

- **书目信息：** Boschi, Ivan; De Toni, A.; Di Leva, Roberto; Ida’, E.; Carricato, Marco（2026），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2026.3653295)。
- **初筛 / 全文状态：** 核心 / `PAYWALLED_OR_UNAVAILABLE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2026.3653295`。
- **摘要精读：** 对 non-cuspidal 串联臂以 Uniqueness Domains 描述分支，给出任务需跨域时越过奇异配置的换支方法，目标保持关节变量连续可微，做模拟和实验比较。
- **与主题的关系：** 最高优先级核心：直接针对穿越奇异时连续可微换支。
- **全文待核：** 摘要未给可行条件、自由度/机构参数、速度/加速度/关节硬界和实验统计。

## 相邻与背景文献摘要卡（74 篇）

### 006. [Existence Conditions and General Solutions of Closed-form Inverse Kinematics for Revolute Serial Robots](https://consensus.app/papers/existence-conditions-and-general-solutions-of-closedform-wang-luo/e336577edbc15f0e8dce768e2ed2e8a4/?utm_source=chatgpt)

- **书目信息：** Wang, Shanda; Luo, Xiao; Luo, Qingsheng; Han, Bao-Ling（2019），Applied Sciences；[DOI](https://doi.org/10.3390/app9204365)。
- **初筛 / 全文状态：** 相邻/背景 / `PAYWALLED_OR_UNAVAILABLE`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/app9204365`。
- **摘要精读：** 按 DH 结构将闭式 IK 化为三类代数子问题，并据此给出通用解析求解程序，主张适用于低自由度串联机器人。
- **与主题的关系：** 解析候选解生成的背景材料，可解释离散分支来源。
- **全文待核：** 不涉及路径跟踪、分支持久化、奇异转换或轨迹约束；不是主题核心证据。

### 007. [Inverse Kinematics for Serial Kinematic Chains via Sum of Squares Optimization](https://consensus.app/papers/inverse-kinematics-for-serial-kinematic-chains-via-sum-of-marić-giamou/8dfca0c662fc56f6b049aedbfa690c13/?utm_source=chatgpt)

- **书目信息：** Marić, Filip; Giamou, Matthew; Khoubyarian, Soroush; Petrović, I.; Kelly, Jonathan（2020），2020 IEEE International Conference on Robotics and Automation (ICRA)；[DOI](https://doi.org/10.1109/icra40945.2020.9196704)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/icra40945.2020.9196704`。
- **摘要精读：** 将球关节串联链的 IK 写成最近点凸优化并用稀疏 SOS 求解，在满足特定条件时证明松弛达到全局最优；含关节限位和开源实现。
- **与主题的关系：** 解析静态 IK 与限位可行性的数学背景，及全局最优证据。
- **全文待核：** 摘要聚焦单目标构型，不报告连续轨迹、分支跟踪或奇异转换；全局最优仅在所述条件下。

### 009. [Online Time-Optimal Trajectory Planning for Robotic Manipulators Using Adaptive Elite Genetic Algorithm With Singularity Avoidance](https://consensus.app/papers/online-timeoptimal-trajectory-planning-for-robotic-liu-guo/d0b72510503c5de7bab9e0b949916a88/?utm_source=chatgpt)

- **书目信息：** Liu, Yi; Guo, Chen; Weng, Yongpeng（2019），IEEE Access；[DOI](https://doi.org/10.1109/access.2019.2945824)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/access.2019.2945824`。
- **摘要精读：** 将 Cartesian 五次多项式轨迹、时间最优优化与自适应精英遗传算法/奇异回避结合，实验比较报告优于基础 GA 及变体。
- **与主题的关系：** 涉及轨迹平滑、时间优化和奇异性回避。
- **全文待核：** 摘要没有给出与 IK 解支跟踪的耦合、关节硬约束或跨奇异转换机制。

### 010. [An Adaptive Second Order Sliding Mode Inverse Kinematics Approach for Serial Kinematic Chain Robot Manipulators](https://consensus.app/papers/an-adaptive-second-order-sliding-mode-inverse-kinematics-elawady-bouteraa/1f1b573287f75ceb9518c268f946f845/?utm_source=chatgpt)

- **书目信息：** Elawady, W.; Bouteraa, Y.; Elmogy, Ahmed（2020），Robotics；[DOI](https://doi.org/10.3390/robotics9010004)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/robotics9010004`。
- **摘要精读：** 提出二阶连续滑模自适应 IK 以补偿串联链 Jacobian 未知不确定性，Lyapunov 分析宣称闭环全局稳定，并用仿真展示鲁棒性。
- **与主题的关系：** 可作为模型不确定时的微分/反馈 IK 背景。
- **全文待核：** 摘要未覆盖离散解支标识、轨迹分支连续性、关节限位或实验验证。

### 011. [An Efficient and Accurate Inverse Kinematics for 7-DOF Redundant Manipulators Based on a Hybrid of Analytical and Numerical Method](https://consensus.app/papers/an-efficient-and-accurate-inverse-kinematics-for-7dof-jin-liu/cad5b0f444205ed2a0410cf9f45cf118/?utm_source=chatgpt)

- **书目信息：** Jin, Ming-He; Liu, Qiang; Wang, Bin; Liu, Hong（2020），IEEE Access；[DOI](https://doi.org/10.1109/access.2020.2966768)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/access.2020.2966768`。
- **摘要精读：** 7-DOF SSRMS 型冗余臂的解析/数值混合 IK：肘向参数化后用 PSO 优化，再加入避障、避奇异和可操作度目标。
- **与主题的关系：** 多解选择和姿态约束与冗余分支选择相关。
- **全文待核：** 摘要仅报运动学仿真；未说明沿轨迹分支不跳变或约束严格保证。

### 012. [DPSO and Inverse Jacobian-Based Real-Time Inverse Kinematics With Trajectory Tracking Using Integral SMC for Teleoperation](https://consensus.app/papers/dpso-and-inverse-jacobianbased-realtime-inverse-khan-abbasi/705a96659c2255fe91a7ed9c24ea4b10/?utm_source=chatgpt)

- **书目信息：** Khan, H.; Abbasi, S.; Lee, Min Choel（2020），IEEE Access；[DOI](https://doi.org/10.1109/access.2020.3020318)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/access.2020.3020318`。
- **摘要精读：** 核设施拆除遥操作中用双 PSO 分开优化位置/姿态，以逆 Jacobian 生成平滑关节轨迹，并用积分滑模控制抗扰；有实验结果。
- **与主题的关系：** 实时 Cartesian 跟踪、关节轨迹平滑及实验背景。
- **全文待核：** 摘要未给出奇异处理、分支追踪或显式关节硬约束。

### 014. [Globally Optimal Solution to Inverse Kinematics of 7DOF Serial Manipulator](https://consensus.app/papers/globally-optimal-solution-to-inverse-kinematics-of-7dof-trutman-din/f39e0a6d80a4580d8e75ad8bad8bbe91/?utm_source=chatgpt)

- **书目信息：** Trutman, Pavel; Din, M. El; Henrion, D.; Pajdla, T.（2022），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2022.3163444)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2022.3163444`。
- **摘要精读：** 将通用 7-DOF 转动关节 IK 化为多项式优化并用 Lasserre 松弛求可认证全局最优或不可行性；KUKA LBR IIWA 测试位姿中 99.9% 可解/判定。
- **与主题的关系：** 静态 IK 与全局最优认证的数学背景，包含关节限位。
- **全文待核：** 不是路径/分支跟踪；99.9% 是测试位姿结果，不能外推为连续轨迹保证。

### 015. [Improved singular robust inverse solutions of redundant serial manipulators](https://consensus.app/papers/improved-singular-robust-inverse-solutions-of-redundant-sun-liu/5642f45eacf45801861c3c7ef3d40eee/?utm_source=chatgpt)

- **书目信息：** Sun, Jingyu; Liu, Yan-Jun; Ji, Chen（2020），International Journal of Advanced Robotic Systems；[DOI](https://doi.org/10.1177/1729881420932046)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1177/1729881420932046`。
- **摘要精读：** 通过修正系数改良奇异鲁棒逆方法，并以 PSO/神经网络自适应调参；Lyapunov 稳定性分析，七轴臂线/曲线轨迹仿真比较误差、最小奇异值和关节角速度。
- **与主题的关系：** 微分 IK 的近奇异鲁棒性和关节速度表现。
- **全文待核：** 摘要只报告仿真；未说明跨奇异转换或分支身份，不能视为路径级保证。

### 018. [A modified firefly algorithm for the inverse kinematics solutions of robotic manipulators](https://consensus.app/papers/a-modified-firefly-algorithm-for-the-inverse-kinematics-hernández-barragán-lópez-franco/852eee893dc7570380e9bac1f653f479/?utm_source=chatgpt)

- **书目信息：** Hernández-Barragán, J.; López-Franco, C.; Arana-Daniel, N.; Alanis, A.; Lopez-Franco, Adriana（2021），Integrated Computer-Aided Engineering；[DOI](https://doi.org/10.3233/ica-210660)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3233/ica-210660`。
- **摘要精读：** 用改进萤火虫多模态优化求多个可达同一末端位姿的构型，避免 Jacobian 求逆并考虑关节限位；有仿真、统计检验和 5-DOF 实时实验。
- **与主题的关系：** 多候选解生成及限位背景。
- **全文待核：** 摘要未说明沿路径持久追踪某一分支；无 Jacobian 求逆不等于保证奇异处可连续通过。

### 019. [A Multiple Solutions Approach to the Inverse Kinematics Problem of a General Serial Manipulator](https://consensus.app/papers/a-multiple-solutions-approach-to-the-inverse-kinematics-fan-li/da80dd2f596f509e8731a99ee2db5dd9/?utm_source=chatgpt)

- **书目信息：** Fan, Yanping; Li, Pin; Zhen, Xijin; Shen, Zongbao（2021），Journal of Physics: Conference Series；[DOI](https://doi.org/10.1088/1742-6596/2002/1/012023)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1088/1742-6596/2002/1/012023`。
- **摘要精读：** 对一般串联机械臂使用多解数值 IK，并以数值例子验证；在奇异位形示例中给出有限个数值解。
- **与主题的关系：** 一般串联机构多解结构与奇异位形背景。
- **全文待核：** 不涉及轨迹级解支连续、约束和实验验证；摘要对奇异位形“有限个解”的机制不足以评价。

### 020. [A Real-Time-Capable Closed-Form Multi-Objective Redundancy Resolution Scheme for Seven-DoF Serial Manipulators](https://consensus.app/papers/a-realtimecapable-closedform-multiobjective-redundancy-wiedmeyer-altoé/8fcb38ea2dae5cc7a6aaffd1be5f642c/?utm_source=chatgpt)

- **书目信息：** Wiedmeyer, Wolfgang; Altoé, Philipp; Auberle, Jonathan; Ledermann, C.; Kröger, Torsten（2021），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2020.3045646)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2020.3045646`。
- **摘要精读：** 为 7-DOF 串联臂解析冗余解加入实时多目标闭式优化，兼顾关节限位并最小化速度/加速度；覆盖完整解空间，开源实现，Cartesian 路径上更快更平滑且做 iiwa 实验。
- **与主题的关系：** 核心：解析冗余分辨与轨迹平滑、关节运动量和限位共同处理。
- **全文待核：** 摘要未交代位置/速度/加速度约束是否硬保证、奇异转换与实验范围。

### 021. [A Solution of the Inverse Kinematics Problem for a 7-Degrees-of-Freedom Serial Redundant Manipulator Using Gröbner Bases Theory](https://consensus.app/papers/a-solution-of-the-inverse-kinematics-problem-for-a-schnitman/8e079c33098754399b09f08ec3be0dc0/?utm_source=chatgpt)

- **书目信息：** Schnitman, L.（2021），Mathematical Problems in Engineering；[DOI](https://doi.org/10.1155/2021/6680687)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1155/2021/6680687`。
- **摘要精读：** 以 Gröbner 基求 7-DOF 串联冗余臂的多个 IK 解，建立 DH 模型并用代数软件核对解。
- **与主题的关系：** 多解候选生成的解析背景。
- **全文待核：** 摘要只报告代数验证；不含路径延续、分支连续或约束保证。

### 022. [An Improved Weighted Gradient Projection Method for Inverse Kinematics of Redundant Surgical Manipulators](https://consensus.app/papers/an-improved-weighted-gradient-projection-method-for-zhang-fan/ac84ca9986395c69bccf5ddab4bbe3c9/?utm_source=chatgpt)

- **书目信息：** Zhang, Xing-Lei; Fan, Bing-Hui; Wang, Chuan-Jiang; Cheng, Xiao-Lin（2021），Sensors (Basel, Switzerland)；[DOI](https://doi.org/10.3390/s21217362)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/s21217362`。
- **摘要精读：** 面向腹腔镜 7-DOF 臂改进加权梯度投影，组合限位/奇异性排斥势场与 DLS 阻尼权重，仿真比较定位姿精度及限位/奇异回避。
- **与主题的关系：** 冗余 IK 中联合关节限位与奇异区域回避的直接相关方法。
- **全文待核：** 证据为仿真；回避奇异不等于跨奇异分支转换，且摘要未说明连续轨迹保证。

### 023. [Collision-free path planning for welding manipulator via hybrid algorithm of deep reinforcement learning and inverse kinematics](https://consensus.app/papers/collisionfree-path-planning-for-welding-manipulator-via-zhong-wang/20c01e653b245360ad68ce96ab8cafee/?utm_source=chatgpt)

- **书目信息：** Zhong, Jie; Wang, Tao; Cheng, Lianglun（2021），Complex & Intelligent Systems；[DOI](https://doi.org/10.1007/s40747-021-00366-1)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1007/s40747-021-00366-1`。
- **摘要精读：** 焊接机械臂用深度强化学习在连续高维关节空间规划避碰路径，将 IK 作为先验并加 gain 模块改善训练；多维路径规划实验。
- **与主题的关系：** 说明 IK 候选如何嵌入路径规划与避碰。
- **全文待核：** 贡献重点是学习式配置空间规划，不是 IK 分支持续跟踪；与固定基座/约束细节需全文确认。

### 024. [IKFlow: Generating Diverse Inverse Kinematics Solutions](https://consensus.app/papers/ikflow-generating-diverse-inverse-kinematics-solutions-ames-morgan/c0ac6aac4ea85f4b9ce40fbc6808a100/?utm_source=chatgpt)

- **书目信息：** Ames, Barrett; Morgan, Jeremy; Konidaris, G.（2021），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2022.3181374)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2022.3181374`。
- **摘要精读：** IKFlow 用深度神经网络快速生成高维 IK 解空间的多样样本，报告每 10 ms 约 2000 个解、误差约 10 mm/2°，可再用经典法细化。
- **与主题的关系：** 可作为多候选解生成模块，为约束选择或避障提供候选。
- **全文待核：** 摘要没有连续轨迹、分支标签或跨奇异性保证；数值指标以摘要陈述为准。

### 025. [Kinematics and Singularity Analysis of a 7-DOF Redundant Manipulator](https://consensus.app/papers/kinematics-and-singularity-analysis-of-a-7dof-redundant-shi-guo/4bdcd7d057fe5ab78a6ef4fa34b3330d/?utm_source=chatgpt)

- **书目信息：** Shi, X.; Guo, Yu; Chen, Xue-Chan; Chen, Zi-Ming; Yang, Zhi-Wei（2021），Sensors (Basel, Switzerland)；[DOI](https://doi.org/10.3390/s21217257)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/s21217257`。
- **摘要精读：** 针对三连续平行轴 7-DOF 臂以冗余角几何求解 IK，推导 Jacobian 奇异条件并映射到任务空间，再用冗余角和末端位姿避奇异；仿真验证。
- **与主题的关系：** 奇异集合的结构化描述和冗余参数化背景。
- **全文待核：** 以回避奇异为主，没有轨迹级解支转换证明或实机证据。

### 028. [PARTICLE SWARM OPTIMIZATION FOR INVERSE KINEMATICS SOLUTION AND TRAJECTORY PLANNING OF 7-DOF AND 8-DOF ROBOT MANIPULATORS BASED ON UNIT QUATERNION REPRESENTATION](https://consensus.app/papers/particle-swarm-optimization-for-inverse-kinematics-abdor-sierra-merchán-cruz/ad711f5d7f5655eaa86b0d7288427bc3/?utm_source=chatgpt)

- **书目信息：** Abdor-Sierra, Javier Alexis; Merchán-Cruz, E.; Sánchez-Garfias, F.; Rodríguez-Cañizo, R.; Portilla-Flores, E.; Vázquez-Castillo, Valentín（2021），Journal of Applied Engineering Science；[DOI](https://doi.org/10.5937/jaes0-30557)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.5937/jaes0-30557`。
- **摘要精读：** 以单位四元数误差为姿态代价，PSO 为 7/8-DOF 机械臂求多解 IK 并逐点做路径规划。
- **与主题的关系：** 高冗余臂上的路径级候选生成。
- **全文待核：** 摘要未说明相邻点解支关联、时间连续性、硬约束或奇异处理保证。

### 029. [Singularity Avoidance of Task-redundant Robots in Pointing Tasks: On Nullspace Projection and Cardan Angles as Orientation Coordinates](https://consensus.app/papers/singularity-avoidance-of-taskredundant-robots-in-schappler-ortmaier/f0eb8537edee5f11a376814300e9334c/?utm_source=chatgpt)

- **书目信息：** Schappler, Moritz; Ortmaier, T.（2021），；[DOI](https://doi.org/10.5220/0010621103380349)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.5220/0010621103380349`。
- **摘要精读：** 面向只需位置和指向的任务冗余，使用 Cardan 角建立一阶/二阶 IK 与零空间性能梯度投影；示例显示可回避并退出并联机器人 II 型奇异。
- **与主题的关系：** 任务冗余和二阶零空间奇异处理可作方法背景。
- **全文待核：** 主要示例是六足并联机器人，serial industrial-arm 证据有限；退出并联奇异不能直接等同于串联 IK 分支过渡。

### 033. [A Novel Solution to the Inverse Kinematics Problem of General 7R Robots](https://consensus.app/papers/a-novel-solution-to-the-inverse-kinematics-problem-of-xie-sun/9ce4c9ec319353888785690afa73539b/?utm_source=chatgpt)

- **书目信息：** Xie, Shuxin; Sun, Lining; Chen, Guodong; Wang, Zhenhua; Wang, Zi-Xiang（2022），IEEE Access；[DOI](https://doi.org/10.1109/access.2022.3184451)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/access.2022.3184451`。
- **摘要精读：** 一般 7R 解析数值混合求解，符号预处理、Sylvester 消元与特征分解生成多个逆解；模拟和实验结果称近实时且稳定。
- **与主题的关系：** 一般 7R 多分支候选的快速生成基础。
- **全文待核：** 摘要未覆盖沿轨迹选择/延续分支或关节硬约束。

### 034. [A review of cuspidal serial and parallel manipulators](https://consensus.app/papers/a-review-of-cuspidal-serial-and-parallel-manipulators-wenger-chablat/d070e4c3a7c85df1add6900c92b5c9d6/?utm_source=chatgpt)

- **书目信息：** Wenger, P.; Chablat, D.（2023），Journal of Mechanisms and Robotics；[DOI](https://doi.org/10.1115/1.4055677)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1115/1.4055677`。
- **摘要精读：** 综述 cuspidal 串联/并联机器人可在不同运动学解之间无奇异转换，梳理识别、结构与轨迹规划问题。
- **与主题的关系：** 奇异性与分支转换分类的关键背景，可区分 cuspidal 与非 cuspidal 机器人的转换机制。
- **全文待核：** 范围也含并联机器人；它是综述，不是固定基座串联臂连续 IK 算法证据。

### 035. [Algorithm for Determining the Types of Inverse Kinematics Solutions for Sequential Planar Robots and Their Representation in the Configuration Space](https://consensus.app/papers/algorithm-for-determining-the-types-of-inverse-kinematics-chavdarov-naydenov/90a458e245e0531ba72918600316ea81/?utm_source=chatgpt)

- **书目信息：** Chavdarov, I.; Naydenov, Bozhidar（2022），Algorithms；[DOI](https://doi.org/10.3390/a15120469)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/a15120469`。
- **摘要精读：** 为平面串联机器人定义 IK 解类型并在工作空间/构型空间绘制可达区域；讨论穿越奇异配置切换解类型。
- **与主题的关系：** 配置空间分支区域与奇异转换的概念背景。
- **全文待核：** 主要是 2/3R 平面几何与程序展示；未给一般 3D 机械臂路径保证。

### 038. [IK-Geo: Unified robot inverse kinematics using subproblem decomposition](https://consensus.app/papers/ikgeo-unified-robot-inverse-kinematics-using-subproblem-elias-wen/8ac04ee704655124ba29e9dbd0043bcf/?utm_source=chatgpt)

- **书目信息：** Elias, Alexander; Wen, John（2025），Mechanism and Machine Theory；[DOI](https://doi.org/10.1016/j.mechmachtheory.2025.105971)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus search result（已另行 fetch 核实题录）；Consensus DOI 匹配：`10.1016/j.mechmachtheory.2025.105971`。
- **摘要精读：** IK-Geo 将 6R 全转动臂的 IK 统一分解成六个几何子问题，处理完整、奇异以及部分最小二乘解；根据轴线结构分类，许多情况闭式无迭代。
- **与主题的关系：** 解析 IK 的全解/奇异解结构背景，有助于理解离散解支的生成。
- **全文待核：** 静态 6R 求解器，不是冗余轨迹分支跟踪或关节约束规划方法。

### 039. [Inverse Kinematics Solution of Articulated Robots Using a Heuristic Approach for Optimizing Joint Displacement](https://consensus.app/papers/inverse-kinematics-solution-of-articulated-robots-using-a-vázquez-castillo-torres-figueroa/885696df80495af0b2859306412e14d7/?utm_source=chatgpt)

- **书目信息：** Vázquez-Castillo, Valentín; Torres-Figueroa, J.; Merchán-Cruz, E.; Vega-Alvarado, Eduardo; Niño-Suárez, P.; Rodríguez-Cañizo, R.（2022），IEEE Access；[DOI](https://doi.org/10.1109/access.2022.3182496)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/access.2022.3182496`。
- **摘要精读：** 离线差分进化沿既定轨迹逐阶段求解 IK，以关节位移最小化并将末端位置/姿态作为等式约束；用相邻路径点暖启动加速，IRB-1600 圆形与 Lissajous 路径以 RoboDK 仿真。
- **与主题的关系：** 轨迹级解连续选择代理（最小关节位移）与奇异规避背景。
- **全文待核：** 摘要未报告全局/硬约束保证；只有模拟案例，没有显式分支状态或实机证据。

### 040. [Machine Learning-based Framework for Optimally Solving the Analytical Inverse Kinematics for Redundant Manipulators](https://consensus.app/papers/machine-learningbased-framework-for-optimally-solving-vu-beck/dd00d24218755d7d99e2e7ead0feee72/?utm_source=chatgpt)

- **书目信息：** Vu, Minh; Beck, F.; Hartl-Nesic, C.; Nguyen, Anhtuan; Kugi, A.（2023），Mechatronics；[DOI](https://doi.org/10.1016/j.mechatronics.2023.102970)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus search result（已另行 fetch 核实题录）；Consensus DOI 匹配：`10.1016/j.mechatronics.2023.102970`。
- **摘要精读：** 对冗余解析 IK 用 redundancy parameters 参数化，再由神经网络根据可操作度和距当前构型的接近程度选取目标解；KUKA iiwa 蒙特卡洛评估，约 32 微秒。
- **与主题的关系：** 当前姿态距离可作为局部解支延续信号，适用于实时轨迹规划。
- **全文待核：** 摘要未给时间序列下的分支不跳变证明、关节硬约束或实验任务评价；蒙特卡洛不是实机轨迹证据。

### 041. [Mapping Robot Singularities through the Monte Carlo Method](https://consensus.app/papers/mapping-robot-singularities-through-the-monte-carlo-stejskal-svetlík/0190cb7bd7a550be88d248b64fbb49f1/?utm_source=chatgpt)

- **书目信息：** Stejskal, T.; Svetlík, J.; Ondočko, Š.（2022），Applied Sciences；[DOI](https://doi.org/10.3390/app12168330)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/app12168330`。
- **摘要精读：** 用 Monte Carlo 随机映射不同机械臂的工作空间，估计轨迹邻域奇异状态及其出现次数，辅助构型与机器人选型。
- **与主题的关系：** 奇异位形地图可用于前期轨迹评估。
- **全文待核：** 不实际求解 IK 轨迹，也不追踪分支或保证约束；方法是采样统计。

### 042. [Meta-Heuristics Based Inverse Kinematics of Robot Manipulator’s Path Tracking Capability Under Joint Limits](https://consensus.app/papers/metaheuristics-based-inverse-kinematics-of-robot-kanagaraj-yu/7c3f776d9418596a8f7b932274e04480/?utm_source=chatgpt)

- **书目信息：** Kanagaraj, G.; Yu, Vincent（2022），MENDEL；[DOI](https://doi.org/10.13164/mendel.2022.1.041)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.13164/mendel.2022.1.041`。
- **摘要精读：** 在关节限位下比较 BAT、GSA、PSO、WOA 四种启发式沿预定义路径求 IK 的仿真精度，报告 BAT/GSA 领先。
- **与主题的关系：** 提供启发式路径 IK 对比背景。
- **全文待核：** 摘要未报告时间连续/分支连续证明、奇异转换或实机验证；启发式比较的指标和公平性待全文核查。

### 043. [Singular Configuration Analysis and Singularity Avoidance with Application in an Intelligent Robotic Manipulator](https://consensus.app/papers/singular-configuration-analysis-and-singularity-wang-zhou/b7ed95861cbf5ab3853fba73ee582820/?utm_source=chatgpt)

- **书目信息：** Wang, Helin; Zhou, Zida; Zhong, X.; Chen, Qi（2022），Sensors (Basel, Switzerland)；[DOI](https://doi.org/10.3390/s22031239)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/s22031239`。
- **摘要精读：** 针对协作机器人用载荷/力矩传感动态模型分析奇异原因，并对点到点和连续路径的奇异回避方案做模拟比较。
- **与主题的关系：** 连续路径中的奇异回避控制与工业协作臂背景。
- **全文待核：** 目标是避开奇异而非穿越并换支；摘要所述证据是仿真。

### 044. [Singularity Analysis and Complete Methods to Compute the Inverse Kinematics for a 6-DOF UR/TM-Type Robot](https://consensus.app/papers/singularity-analysis-and-complete-methods-to-compute-the-villalobos-sanchez/2df7e142c9785d3ebe68ae592caef339/?utm_source=chatgpt)

- **书目信息：** Villalobos, Jessica; Sanchez, Irma; Martell, F.（2022），Robotics；[DOI](https://doi.org/10.3390/robotics11060137)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/robotics11060137`。
- **摘要精读：** 为 UR5 建完整 IK 与奇异分析，提出枚举解集或有限状态机逐步选择解支，目的在于连续运动、避免突变并避奇异；摘要称多数时候选择一致。
- **与主题的关系：** 强核心：显式利用离散解和状态机追踪以减少关节跳变。
- **全文待核：** “连续”指标、失败边界与约束保证未知；策略是回避奇异，不是奇异跨越。

### 047. [A Concurrent Framework for Constrained Inverse Kinematics of Minimally Invasive Surgical Robots](https://consensus.app/papers/a-concurrent-framework-for-constrained-inverse-colan-davila/ab8e4d8f22b95b68a79e509ba3351e2e/?utm_source=chatgpt)

- **书目信息：** Colan, Jacinto; Davila, Ana; Fozilov, Khusniddin; Hasegawa, Y.（2023），Sensors (Basel, Switzerland)；[DOI](https://doi.org/10.3390/s23063328)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/s23063328`。
- **摘要精读：** 面向微创手术 RCM 约束，结合逆 Jacobian 与层次 QP 并发求解器，把 RCM 和关节限位放入优化；仿真和真实任务实验报告求解率与时延改善。
- **与主题的关系：** 约束型串联 IK 与并行/分层求解策略的工程证据。
- **全文待核：** RCM 手术任务专用；摘要未报告连续解支追踪或奇异转换。

### 049. [A Time-Optimal Continuous Jerk Trajectory Planning Algorithm for Manipulators](https://consensus.app/papers/a-timeoptimal-continuous-jerk-trajectory-planning-zhou-han/83d26f869aba5d7c8a11d5e06dbd63e9/?utm_source=chatgpt)

- **书目信息：** Zhou, Yaosheng; Han, Guirong; Wei, Ziang; Huang, Zixin; Chen, Xubing（2023），Applied Sciences；[DOI](https://doi.org/10.3390/app132011479)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/app132011479`。
- **摘要精读：** 先为指定任务路径取关节位置序列，再用七次 B 样条使速度、加速度、jerk 连续，控制点承载运动学约束并用 SQP 优化最短时间；仿真。
- **与主题的关系：** 强调分支选择之后的连续高阶关节轨迹时间参数化。
- **全文待核：** 摘要没说明怎样选 IK 分支、检测跳变或处理奇异；只报告模拟。

### 050. [Adaptive Manipulability-Based Path Planning Strategy for Industrial Robot Manipulators](https://consensus.app/papers/adaptive-manipulabilitybased-path-planning-strategy-for-shen-xie/de8129700092512992e8951e90544d74/?utm_source=chatgpt)

- **书目信息：** Shen, Henghua; Xie, Wen-Fang; Tang, Jianyu; Zhou, Tao（2023），IEEE/ASME Transactions on Mechatronics；[DOI](https://doi.org/10.1109/tmech.2022.3231467)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tmech.2022.3231467`。
- **摘要精读：** 工业臂用可操作度约束的 RRT* 找短路径，闭环约束 IK 分配冗余提高可操作度并避配置奇异；六轴 FANUC 模拟/实验。
- **与主题的关系：** 路径几何与可操作度/奇异回避联合规划的实验证据。
- **全文待核：** 方法重心是 RRT* 路径和奇异回避，不是 IK 解支连续转换；六轴机型无冗余空间需留意。

### 051. [An Analytical Solution for Inverse Kinematics of SSRMS-Type Redundant Manipulators](https://consensus.app/papers/an-analytical-solution-for-inverse-kinematics-of-qin-wei/8037b6b89a575149add4064c1d5b7436/?utm_source=chatgpt)

- **书目信息：** Qin, Li; Wei, Xiao-Peng; Lv, Liangliang; Han, Liangliang; Fang, Guangqiang（2023），Sensors (Basel, Switzerland)；[DOI](https://doi.org/10.3390/s23125412)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/s23125412`。
- **摘要精读：** 为 SSRMS/SRS 七轴冗余臂施加对齐约束把空间 IK 分为三个平面子问题，可生成最多 16 组解，并讨论奇异构型与不可达位姿；模拟并评估含奇异配置的轨迹。
- **与主题的关系：** 解析多分支枚举与奇异轨迹规划的核心候选。
- **全文待核：** 摘要没有给连续换支规则、奇异穿越的连续阶数或实机验证。

### 052. [An iterative path-following method for hyper-redundant snake-like manipulator with joint limits](https://consensus.app/papers/an-iterative-pathfollowing-method-for-hyperredundant-wang-xie/c27e9abb0483538598f5fce57b90eee9/?utm_source=chatgpt)

- **书目信息：** Wang, Cheng; Xie, Hai-Bo; Yang, Huayong（2023），Ind. Robot；[DOI](https://doi.org/10.1108/ir-04-2022-0106)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1108/ir-04-2022-0106`。
- **摘要精读：** 蛇形超冗余臂用几何逐点路径跟随并迭代调整关节直至限位满足，再解析求 IK；12-DOF 模拟/实验报告速度、精度和限位。
- **与主题的关系：** 路径跟踪与显式关节限位的工程证据。
- **全文待核：** 对象为拉索驱动蛇形臂，开环且弹性引入误差；与常规工业串联臂外推有限。

### 054. [DawnIK: Decentralized Collision-Aware Inverse Kinematics Solver for Heterogeneous Multi-Arm Systems](https://consensus.app/papers/dawnik-decentralized-collisionaware-inverse-kinematics-marangoz-menon/b0ad017f38055e06bf01b1e49e504f6e/?utm_source=chatgpt)

- **书目信息：** Marangoz, S.; Menon, Rohit; Dengler, Nils; Bennewitz, Maren（2023），2023 IEEE-RAS 22nd International Conference on Humanoid Robots (Humanoids)；[DOI](https://doi.org/10.1109/humanoids57100.2023.10375189)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/humanoids57100.2023.10375189`。
- **摘要精读：** DawnIK 以加权非线性优化求多台串联臂的自碰/臂间避碰 IK，可不要求冗余度并支持分散式同时轨迹跟踪；实验场景无碰撞。
- **与主题的关系：** 多臂环境中的约束 IK 与轨迹跟踪。
- **全文待核：** 主贡献是碰撞协调，不是单臂分支连续/奇异转换；是否贴合固定基座范围需全文审查。

### 055. [Direct Collocation Methods for Trajectory Optimization in Constrained Robotic Systems](https://consensus.app/papers/direct-collocation-methods-for-trajectory-optimization-bordalba-schoels/06c120d74d265c9fa33b6aa7edc9b26b/?utm_source=chatgpt)

- **书目信息：** Bordalba, Ricard; Schoels, Tobias; Ros, L.; Porta, J.; Diehl, M.（2023），IEEE Transactions on Robotics；[DOI](https://doi.org/10.1109/tro.2022.3193776)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tro.2022.3193776`。
- **摘要精读：** 研究直接配点在受约束机器人系统中的离散轨迹偏离约束流形问题，综述并提出可消除离散甚至连续漂移的方法。
- **与主题的关系：** 约束轨迹优化的数值误差背景，可影响跟踪可行性。
- **全文待核：** 不是 IK 分支追踪论文，讨论更广泛的闭链/滚动接触系统。

### 057. [Inverse kinematics and path planning of manipulator using real quantifier elimination based on Comprehensive Gröbner Systems](https://consensus.app/papers/inverse-kinematics-and-path-planning-of-manipulator-using-yoshizawa-terui/664ecb8d8040553da095634dd95f6025/?utm_source=chatgpt)

- **书目信息：** Yoshizawa, M.; Terui, Akira; Mikawa, M.（2023），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2305.12451)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2305.12451`。
- **摘要精读：** 用基于 Comprehensive Gröbner Systems 的实量词消去求 3-DOF IK，并对参数化整条路径验证 IK 解存在，避免重复计算；含计算例与实验。
- **与主题的关系：** 重要的全路径可达性/存在性证书背景。
- **全文待核：** 存在某解不等于同一连续解支全程存在；摘要未说明分支延续、关节运动限值和实验范围。

### 058. [Inverse Kinematics of an Anthropomorphic 6R Robot Manipulator Based on a Simple Geometric Approach for Embedded Systems](https://consensus.app/papers/inverse-kinematics-of-an-anthropomorphic-6r-robot-anschober-edlinger/3cd2a9caf4125f348226ce801c81c5d1/?utm_source=chatgpt)

- **书目信息：** Anschober, Michael; Edlinger, R.; Froschauer, R.; Nuechter, A.（2023），Robotics；[DOI](https://doi.org/10.3390/robotics12040101)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/robotics12040101`。
- **摘要精读：** 为嵌入式 6R 工业臂以几何关系构造快速闭式 IK，分析奇异、限位、工作空间与可解性，并在嵌入式硬件验证。
- **与主题的关系：** 边缘算力下解析候选计算与可解性背景。
- **全文待核：** 单点 IK 求解器；没有轨迹分支一致性或约束穿越证据。

### 059. [Kinematically Constrained Jerk–Continuous S-Curve Trajectory Planning in Joint Space for Industrial Robots](https://consensus.app/papers/kinematically-constrained-jerk–continuous-scurve-wu-zhang/3657aeb737f45404bb2be2d9857514a6/?utm_source=chatgpt)

- **书目信息：** Wu, Guanglei; Zhang, Ning（2023），Electronics；[DOI](https://doi.org/10.3390/electronics12051135)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/electronics12051135`。
- **摘要精读：** 以四阶 S 曲线生成关节空间 jerk 连续、多轴同步轨迹，使用多项式方程实现实时运动学约束且无需迭代。
- **与主题的关系：** 关节空间连续性和 jerk 约束的轨迹生成背景。
- **全文待核：** 摘要未涉及如何由 Cartesian 路径选定/延续 IK 解支或奇异变化。

### 060. [Manipulability maximization in constrained inverse kinematics of surgical robots](https://consensus.app/papers/manipulability-maximization-in-constrained-inverse-colan-davila/b02ac8551ccf5945a862f0f822ef706a/?utm_source=chatgpt)

- **书目信息：** Colan, Jacinto; Davila, Ana; Hasegawa, Y.（2023），2023 IEEE International Conference on Mechatronics and Automation (ICMA)；[DOI](https://doi.org/10.1109/icma57826.2023.10215986)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/icma57826.2023.10215986`。
- **摘要精读：** 微创手术约束 IK 用 HQP 分层优化可操作度，同时满足 RCM 和关节限位；6D 路径跟踪仿真平均每次求解低于 1 ms。
- **与主题的关系：** 路径级受约束冗余 IK、任务优先级与实时性的背景。
- **全文待核：** 手术 RCM 专用且摘要所述为仿真；不分析解支连续或奇异跨越。

### 061. [Many Faces of Singularities in Robotics](https://consensus.app/papers/many-faces-of-singularities-in-robotics-dulęba-karcz-dulęba/bbaaee10c4055127baa7705754826481/?utm_source=chatgpt)

- **书目信息：** Dulęba, I.; Karcz-Dulęba, I.（2023），Pomiary Automatyka Robotyka；[DOI](https://doi.org/10.14313/par_247/19)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.14313/par_247/19`。
- **摘要精读：** 教学性综述，从串联臂 IK、非完整运动规划、最优控制等角度分类奇异性，讨论物理/数值意义、检测与处理。
- **与主题的关系：** 奇异类型与检测/回避的概念框架。
- **全文待核：** 范围宽于固定基座串联臂轨迹 IK；综述不提供新算法的直接验证。

### 063. [Obstacle Avoidance in Operational Configuration Space Kinematic Control of Redundant Serial Manipulators](https://consensus.app/papers/obstacle-avoidance-in-operational-configuration-space-peidró-haug/ed23abafe76e5f618f97bf3b30c8eb0a/?utm_source=chatgpt)

- **书目信息：** Peidró, Adrián; Haug, Edward（2023），Machines；[DOI](https://doi.org/10.3390/machines12010010)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/machines12010010`。
- **摘要精读：** 以可微流形形式在 operational configuration space 做冗余串联臂运动学控制与避障，分别示范 4 与 20 个冗余自由度跟踪指定输出轨迹。
- **与主题的关系：** 全局逆映射/配置空间几何与高冗余路径跟踪相关。
- **全文待核：** 摘要没有位置/速度硬限位或奇异转换评估；示例/保证范围须全文核实。

### 064. [Path-Constrained and Collision-Free Optimal Trajectory Planning for Robot Manipulators](https://consensus.app/papers/pathconstrained-and-collisionfree-optimal-trajectory-wen-pagilla/cd2c658f468c5426bd7effeb4e0e8f8c/?utm_source=chatgpt)

- **书目信息：** Wen, Yalun; Pagilla, P.（2023），IEEE Transactions on Automation Science and Engineering；[DOI](https://doi.org/10.1109/tase.2022.3169989)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tase.2022.3169989`。
- **摘要精读：** 给定离散关节位形路点后，用正交配点同时求时间与 jerk 最优、静态避障且满足运动学/动力学约束的轨迹；六轴机器人模拟与实验。
- **与主题的关系：** 多约束轨迹可执行性和碰撞检测的实验证据。
- **全文待核：** IK 分支已由输入路点固定；不解决 Cartesian 路径到连续分支的选择。

### 065. [Redundancy parameterization and inverse kinematics of 7-DOF revolute manipulators](https://consensus.app/papers/redundancy-parameterization-and-inverse-kinematics-of-elias-wen/5bb2c487b6295d90906a79298e550b6b/?utm_source=chatgpt)

- **书目信息：** Elias, Alexander; Wen, John（2023），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2307.13122)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2307.13122`。
- **摘要精读：** 提出广义 SEW 冗余角用于 7R 参数化，构造 stereographic SEW 把算法奇异从工作空间一条线缩到可移出的半线，并证明任一参数化均不可避免出现该类奇异；配套稳健 IK。
- **与主题的关系：** 核心数学背景：冗余参数化及其算法奇异对轨迹延续的限制。
- **全文待核：** 主要给静态 7R IK；没有连续轨迹/关节动态约束保证。

### 066. [Singularity-Robust Inverse Kinematics for Serial Manipulators](https://consensus.app/papers/singularityrobust-inverse-kinematics-for-serial-dulęba/707c73ac46815ab5ba6e4d9ce6852ae3/?utm_source=chatgpt)

- **书目信息：** Dulęba, I.（2023），Journal of Automation, Mobile Robotics and Intelligent Systems；[DOI](https://doi.org/10.14313/jamris/3-2023/21)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.14313/jamris/3-2023/21`。
- **摘要精读：** 针对串联臂奇异鲁棒 IK 作方法指南，比较加性/乘性/SVD 正则化与两种等价奇异回避表述（修改可操作度矩阵或维持最小奇异值阈值），含理论和仿真比较。
- **与主题的关系：** 奇异值阈值与鲁棒微分 IK 的基准/术语参考。
- **全文待核：** 摘要描述奇异回避而非跨奇异换支；具体适用前提需全文看。

### 068. [An Efficient Inverse Kinematic Method for SSRMS-type Manipulator with Conformal Geometric Algebra](https://consensus.app/papers/an-efficient-inverse-kinematic-method-for-ssrmstype-zhao-zhang/b9e9c8924caa56c39ba307ade5f18db2/?utm_source=chatgpt)

- **书目信息：** Zhao, Jingdong; Zhang, Jiayu; Zhao, Liangliang; Tian, Zhong-Lai; Wang, Zirui; Jiang, Wei; Liu, Hong（2024），2024 IEEE International Conference on Advanced Intelligent Mechatronics (AIM)；[DOI](https://doi.org/10.1109/aim55361.2024.10637038)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/aim55361.2024.10637038`。
- **摘要精读：** SSRMS 七轴臂用三连续平行连杆方向向量参数化解析冗余解，并依轨迹上下文点选最优参数；路径跟踪实验证实七关节随最优构型连续变化。
- **与主题的关系：** 强核心：轨迹上下文驱动的解析分支/冗余参数选择，并有连续跟踪实验。
- **全文待核：** 摘要未明确奇异边界或关节硬约束保障；机构范围为特定 SSRMS 类结构。

### 069. [An explicit solution of forward and inverse kinematics for a serial manipulator with insufficient intersection joints based on finite and instantaneous screw theory](https://consensus.app/papers/an-explicit-solution-of-forward-and-inverse-kinematics-for-qi-zhang/e216054e85bf53fa87aa0eff8a577fb7/?utm_source=chatgpt)

- **书目信息：** Qi, Yang; Zhang, Sen; Ren, Xiaofei; Tong, Xinran; Liang, D.; Han, Lin（2024），International Journal of Advanced Robotic Systems；[DOI](https://doi.org/10.1177/17298806241245810)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1177/17298806241245810`。
- **摘要精读：** 对端部关节不相交的特殊串联机构用有限/瞬时螺旋理论与新 Paden–Kahan 子问题推导显式正逆解；数值仿真验证。
- **与主题的关系：** 特殊拓扑的解析 IK 结构背景。
- **全文待核：** 不是常规轨迹分支跟踪；只报告数值例。

### 070. [Automatic Geometric Decomposition for Analytical Inverse Kinematics](https://consensus.app/papers/automatic-geometric-decomposition-for-analytical-ostermeier-külz/40aa6637d6235e0da6bbb273868083e8/?utm_source=chatgpt)

- **书目信息：** Ostermeier, D.; Külz, Jonathan; Althoff, Matthias（2024），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2025.3597897)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2025.3597897`。
- **摘要精读：** 按机器人运动学分类，在线自动把解析 IK 分解为已求解的稳定子问题，报告亚毫秒推导/求解并提供开源工具。
- **与主题的关系：** 高效解析候选生成与可复现实现。
- **全文待核：** 静态 IK 计算性能，不处理沿轨迹分支连续或联合关节限位。

### 072. [Combining closed-form and numerical solutions for the inverse kinematics of six-degrees-of-freedom collaborative handling robot](https://consensus.app/papers/combining-closedform-and-numerical-solutions-for-the-chen-cui/621864edc72d5d189393afdc2c8ed041/?utm_source=chatgpt)

- **书目信息：** Chen, Ya; Cui, Zhi-Guo; Wang, Xiao; Wang, Dianjun; Wang, Zilong; Song, Zhihu; Liu, Ding（2024），International Journal of Advanced Robotic Systems；[DOI](https://doi.org/10.1177/17298806241228372)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1177/17298806241228372`。
- **摘要精读：** 六轴协作臂结合闭式 IK 与 SVD 稳定化 Jacobian/牛顿迭代，轨迹规划实验报告实时平滑运动。
- **与主题的关系：** 混合解析/数值 IK 及轨迹控制背景。
- **全文待核：** 摘要未报告离散分支标签、限位硬约束或奇异转换保证。

### 073. [Dynamic Programming-Based Offline Redundancy Resolution of Redundant Manipulators Along Prescribed Paths with Real-Time Adjustment](https://consensus.app/papers/dynamic-programmingbased-offline-redundancy-resolution-yin-wu/a54604d32d3a521abcf4b08996ff33cf/?utm_source=chatgpt)

- **书目信息：** Yin, Zhihang; Wu, Fa; Wang, Ziqiang; Yang, Jianmin; Tan, Jiyong; Kong, Dexing（2024），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2411.17052)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2411.17052`。
- **摘要精读：** 先离线 DP 规划预设路径冗余解，再在线沿路径法向调整；相邻采样点调整系数变化受全局最大值限制，形成离线/在线融合。
- **与主题的关系：** 以离散 DP 预估后续约束余量并在线调整路径的相关策略。
- **全文待核：** 保证依赖采样点和调整系数变化界；不是连续分支证明，约束类型与实验范围待全文核查。

### 074. [Extended Operational Space Kinematics, Dynamics, and Control of Redundant Serial Robots](https://consensus.app/papers/extended-operational-space-kinematics-dynamics-and-haug-sapio/bc5f406f711a555e8a02a89448205a3a/?utm_source=chatgpt)

- **书目信息：** Haug, Edward; De Sapio, Vincent; Peidró, Adrián（2024），Robotics；[DOI](https://doi.org/10.3390/robotics13120170)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/robotics13120170`。
- **摘要精读：** 以微分几何的任务坐标与自运动坐标建立冗余串联臂操作空间动力学和控制 ODE，处理期望轨迹、避障与性能约束；示例覆盖 1 与 8 个冗余自由度。
- **与主题的关系：** 显式自运动坐标有助于建模冗余分支连续演化。
- **全文待核：** 摘要未报告关节硬界、奇异转换或实机；优越性以示例比较为主。

### 077. [Online Trajectory Generation With Local Replanning for 7-DoF Serial Manipulator in Unforeseen Dynamic Environments](https://consensus.app/papers/online-trajectory-generation-with-local-replanning-for-shao-zhang/1747f5915bbc51028cd68e74f313b033/?utm_source=chatgpt)

- **书目信息：** Shao, Jun; Zhang, Haoyang; Zhu, Shiqiang; Song, Wei（2024），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2024.3450289)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2024.3450289`。
- **摘要精读：** 用一般 7-DOF 拟人机械臂解析几何 IK，把 Cartesian 连杆避障映到关节空间，扩展成动态障碍下在线局部重规划；仿真和实机测试考虑机械限位。
- **与主题的关系：** 实时轨迹跟踪、动态重规划、解析冗余 IK 结合的直接工程候选。
- **全文待核：** 摘要未明确持久分支标签或奇异穿越；碰撞约束保证和限位数学形式需全文核查。

### 079. [Real-time inverse kinematics for robotic manipulation under remote center-of-motion constraint using memetic evolution](https://consensus.app/papers/realtime-inverse-kinematics-for-robotic-manipulation-davila-colan/c97c6dc9d7225d1581b9fb810216a388/?utm_source=chatgpt)

- **书目信息：** Davila, Ana; Colan, Jacinto; Hasegawa, Yasuhisa（2024），J. Comput. Des. Eng.；[DOI](https://doi.org/10.1093/jcde/qwae047)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1093/jcde/qwae047`。
- **摘要精读：** PivotIK 将演化搜索与多目标 Jacobian 优化结合，在冗余手术机器人路径中实时满足 RCM，报告 <1 ms、跟踪/RCM误差和实机实验。
- **与主题的关系：** 受约束实时 IK 与连续轨迹跟踪的实验证据。
- **全文待核：** RCM 手术任务专用，未讨论奇异跨越或解支标签；属于相邻应用。

### 080. [Real-time optimized inverse kinematics of redundant robots under inequality constraints](https://consensus.app/papers/realtime-optimized-inverse-kinematics-of-redundant-zhang-du/4daa1d17d3b554e48ecaad4139126d13/?utm_source=chatgpt)

- **书目信息：** Zhang, Linlin; Du, Huibin; Qin, Z.; Zhao, Yue-Jing; Yang, Guang（2024），Scientific Reports；[DOI](https://doi.org/10.1038/s41598-024-81174-8)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1038/s41598-024-81174-8`。
- **摘要精读：** 用受约束线性规划做冗余 IK，把关节/Cartesian 位置范围及速度、加速度硬边界写成不等式，声称实时执行中绝不违反；KUKA IIWA 仿真与实验。
- **与主题的关系：** 核心约束方法，直接覆盖位置、速度、加速度硬约束。
- **全文待核：** 摘要没有说明解支连续或奇异换支；硬界结论需查完整算法假设、离散模型及实验统计。

### 081. [Simple Inverse Kinematics Computation Considering Joint Motion Efficiency](https://consensus.app/papers/simple-inverse-kinematics-computation-considering-joint-yonezawa-yonezawa/9c26a3cf88e3599c85b41166495bed2a/?utm_source=chatgpt)

- **书目信息：** Yonezawa, Ansei; Yonezawa, Heisei; Kajiwara, Itsuro（2024），IEEE Transactions on Cybernetics；[DOI](https://doi.org/10.1109/tcyb.2024.3372989)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/tcyb.2024.3372989`。
- **摘要精读：** 以 NLSPSA 数值优化同时考虑末端位姿误差与各关节运动效率，冗余臂数值例验证。
- **与主题的关系：** 求解器代价可显式偏好较小/高效关节运动。
- **全文待核：** 没有轨迹分支连续、约束硬保证或实验信息。

### 082. [Towards accuracy improvement in solution of inverse kinematic problem in redundant robot: A comparative analysis](https://consensus.app/papers/towards-accuracy-improvement-in-solution-of-inverse-khaleel-humaidi/f1fe9691085c5373ac252645155062eb/?utm_source=chatgpt)

- **书目信息：** Khaleel, H.; Humaidi, A.（2024），International Review of Applied Sciences and Engineering；[DOI](https://doi.org/10.1556/1848.2023.00722)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1556/1848.2023.00722`。
- **摘要精读：** 对 3-DOF 冗余臂用 NNGA 和 PSO 解三角、圆、正弦轨迹 IK，仿真比较精度，PSO 提升幅度较小。
- **与主题的关系：** 算法基准对照，说明单靠末端精度指标的局限。
- **全文待核：** 仅三自由度仿真，未谈分支、奇异过渡、关节边界；主题相关性较弱。

### 083. [A Decade of Inverse Kinematics Methods for Serial Manipulators: A Systematic Review](https://consensus.app/papers/a-decade-of-inverse-kinematics-methods-for-serial-narayan-gritli/0ecb577cd2c35a8695f498fff6f49c41/?utm_source=chatgpt)

- **书目信息：** Narayan, Jyotindra; Gritli, Hassène; Dwivedy, S.（2025），Journal of Field Robotics；[DOI](https://doi.org/10.1002/rob.70014)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1002/rob.70014`。
- **摘要精读：** 系统综述 2014–2023 串联臂 IK 方法，按模型驱动/数据驱动分类，PRISMA 收集筛选约 321 篇。
- **与主题的关系：** 可用于综述背景分类、比较常见数值/解析/学习 IK 方法。
- **全文待核：** 覆盖一般单点 IK，不能替代面向 trajectory-consistent branch tracking 的专门综合。

### 084. [A Fast and Robust Multistage Hybrid Algorithm for Inverse Kinematics of Redundant Mill Relining Manipulator](https://consensus.app/papers/a-fast-and-robust-multistage-hybrid-algorithm-for-inverse-wang-xue/2d9692cff9e55cdaa8eb87786a346728/?utm_source=chatgpt)

- **书目信息：** Wang, Mingyuan; Xue, Yu-Jun; Li, Jishun; Li, Shuai; Bai, Yunhua（2025），Journal of Field Robotics；[DOI](https://doi.org/10.1002/rob.70130)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1002/rob.70130`。
- **摘要精读：** 为特殊受限空间内磨机衬板操作 7-DOF 臂提出多阶段 IK：循环坐标下降、Halley 快速收敛、全局搜索与关节限位/避碰；含消融、13 种比较和数字孪生硬件试验。
- **与主题的关系：** 受限工作空间中的可行性、速度、关节限制与避碰工程证据。
- **全文待核：** 摘要指出解多样性不足，专用机构；不证明轨迹分支连续或奇异转换。

### 085. [BoundPlanner: A Convex-Set-Based Approach to Bounded Manipulator Trajectory Planning](https://consensus.app/papers/boundplanner-a-convexsetbased-approach-to-bounded-oelerich-hartl-nesic/cb38ca71376359a2938246647ca5b990/?utm_source=chatgpt)

- **书目信息：** Oelerich, Thies; Hartl-Nesic, Christian; Beck, F.; Kugi, Andreas（2025），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2025.3558450)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2025.3558450`。
- **摘要精读：** BoundPlanner 用凸集表达无碰空间和有界 Cartesian 参考路径，再由 BoundMPC 在界内优化跟踪并处理全身碰撞/机器人运动限制；7-DOF 仿真和实验。
- **与主题的关系：** 强相关的在线路径边界、碰撞与运动约束规划。
- **全文待核：** 沿路径优化但未明确持久 IK 解支或跨奇异保证。

### 086. [Fast Path Planning for Kinematic Smoothing of Robotic Manipulator Motion](https://consensus.app/papers/fast-path-planning-for-kinematic-smoothing-of-robotic-liu-li/3c563ffbb107584aa27b0dfa79e8143c/?utm_source=chatgpt)

- **书目信息：** Liu, Hui; Li, Yunfan; Yang, Zhaofeng; Shen, Yue（2025），Sensors (Basel, Switzerland)；[DOI](https://doi.org/10.3390/s25175598)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/s25175598`。
- **摘要精读：** 改进双向 RRT* 并结合 jerk 连续 S 曲线平滑，将几何路径规划接到可执行运动；四个场景仿真报告规划时间/路径代价下降。
- **与主题的关系：** 几何路径与运动学平滑的衔接背景。
- **全文待核：** 不是 IK 解支解析方法；证据仅模拟，任务也偏农业机器人。

### 087. [J-PARSE: Jacobian-based Projection Algorithm for Resolving Singularities Effectively in Inverse Kinematic Control of Serial Manipulators](https://consensus.app/papers/jparse-jacobianbased-projection-algorithm-for-resolving-guptasarma-strong/c916b0765bb351f9adaba707d9fdf370/?utm_source=chatgpt)

- **书目信息：** Guptasarma, Shivani; Strong, M.; Zhen, Honghao; Kennedy, Monroe（2025），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2505.00306)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2505.00306`。
- **摘要精读：** J-PARSE 以保持 manipulability ellipsoid 形状比例的 safety Jacobian 分解任务方向，在奇异方向缩放命令，实现低秩位形进出时平滑的一阶 IK 控制。
- **与主题的关系：** 核心奇异过渡控制：明确报告进出低秩状态的稳定性。
- **全文待核：** 保证明确排除关节限位和碰撞；速度控制，目标是可达/不可达末端位姿而非完整关节路径。

### 088. [Path Planning and Optimization for Cuspidal 6R Manipulators](https://consensus.app/papers/path-planning-and-optimization-for-cuspidal-6r-elias-wen/019bd42d3d7f52908d71f5d2575d22de/?utm_source=chatgpt)

- **书目信息：** Elias, Alexander; Wen, John（2025），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2501.18505)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2501.18505`。
- **摘要精读：** 对 cuspidal 6R 臂逐路径点枚举 IK 解并构图，以关节速度等权重求最短可行路径；可找到非奇异换支或平滑穿越奇异的路径，并优化基座坐标下工具路径偏移。
- **与主题的关系：** 高度核心：分支图搜索、cuspidal 非奇异换支与奇异穿越的统一路径规划。
- **全文待核：** 结论针对 cuspidal 机构；连续性/奇异通过的边构造和动力学关节界细节待全文。

### 089. [Redundancy-Based Motion Planning with Task Constraints for Robot Manipulators](https://consensus.app/papers/redundancybased-motion-planning-with-task-constraints-zhang-wang/51a341359fe0595f91977df01a700be3/?utm_source=chatgpt)

- **书目信息：** Zhang, Yi; Wang, Hong-Guang（2025），Sensors (Basel, Switzerland)；[DOI](https://doi.org/10.3390/s25061900)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/s25061900`。
- **摘要精读：** 为 7-DOF 臂在任务约束下解析生成 Cartesian/关节多解节点，剔除奇异节点并在约束流形邻近节点间构造避碰平滑路径；含模拟/实验。
- **与主题的关系：** 核心：多候选解节点图与任务/碰撞约束下的关节路径连接。
- **全文待核：** 摘要未说明路径全局证明、速度/加速度限制或奇异穿越；策略是移除奇异节点。

### 090. [Time-Jerk Optimal Robotic Trajectory Planning Under Jerk and Continuity Constraints via Convex Optimization](https://consensus.app/papers/timejerk-optimal-robotic-trajectory-planning-under-jerk-qian-yao/edfd2367549752b39ef92cd5e008c51e/?utm_source=chatgpt)

- **书目信息：** Qian, Chen; Yao, Jianjun; Zhang, Yi-Kun（2025），Actuators；[DOI](https://doi.org/10.3390/act14060272)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/act14060272`。
- **摘要精读：** 将任务路径的关节/Cartesian 动静约束纳入时间最优优化，以分段三次样条和连续约束实现关节 C3，再将非凸 jerk 约束凸化为两个 SOCP；有实验。
- **与主题的关系：** 关节高阶连续性与时间/jerk 约束的下游轨迹生成。
- **全文待核：** 摘要不说明 IK 解支怎样产生或维持，也未给奇异转换。

### 091. [Trajectory Tracking Control of a Tendon-Actuated Manipulator with Rolling Joints](https://consensus.app/papers/trajectory-tracking-control-of-a-tendonactuated-hansen-pettersen/2091a2fbf35453f3a45c156591ff49ac/?utm_source=chatgpt)

- **书目信息：** Hansen, Harald; Pettersen, K.; Gravdahl, J.; Di Castro, M.（2025），IFAC-PapersOnLine；[DOI](https://doi.org/10.1016/j.ifacol.2025.10.210)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus search result（已另行 fetch 核实题录）；Consensus DOI 匹配：`10.1016/j.ifacol.2025.10.210`。
- **摘要精读：** 对带滚动关节的拉索驱动新型机械臂导出位置/微分 IK，把耦合关节按平面 2-DOF 连续体处理并用自适应 super-twisting 控制；圆轨迹仿真。
- **与主题的关系：** 连续轨迹 IK 控制背景。
- **全文待核：** 特殊连续体式机构、证据仅模拟；不谈离散分支/奇异/硬关节限制。

### 092. [A Closed-Form Inverse Kinematic Analytical Method for a Humanoid Seven-DOF Redundant Manipulator](https://consensus.app/papers/a-closedform-inverse-kinematic-analytical-method-for-a-zhao-ye/621a0cb1dfc05b8f810a9996c396c946/?utm_source=chatgpt)

- **书目信息：** Zhao, Guojun; Ye, Ben; Tian, Yun-Long; Yun, Juntong; Jiang, Du; Tao, Bo（2026），Machines；[DOI](https://doi.org/10.3390/machines14040395)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/machines14040395`。
- **摘要精读：** 为 7-DOF 拟人臂扩展肩肘腕全局构型参数化，建模含不连通可行臂角区间，并对可行区间做一维解析/区间优化选解；实验跟踪及随机目标比较。
- **与主题的关系：** 核心：分支/构型显式控制、限位可行区间和轨迹跟踪。
- **全文待核：** 摘要未说明跨奇异的连续连接条件、硬动态约束与路径完整覆盖。

### 093. [A Framework for Combining Optimization-Based and Analytic Inverse Kinematics](https://consensus.app/papers/a-framework-for-combining-optimizationbased-and-analytic-cohn-tang/f583d34f82685ceaadc1d59fd3770348/?utm_source=chatgpt)

- **书目信息：** Cohn, Thomas; Tang, Li; Amice, Alexandre; Tedrake, Russ（2026），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2602.05092)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2602.05092`。
- **摘要精读：** 将解析 IK 作为优化变量变换，使带避碰/抓取/人形稳定性约束的非凸优化更易求解；多类优化器实验比较求解率。
- **与主题的关系：** 把解析分支候选嵌入约束优化的通用框架。
- **全文待核：** 摘要未明确沿轨迹分支连续或位置/速度约束；任务种类宽于固定基串联路径。

### 095. [Actuator-Aware Inverse Kinematics with Joint-Limit Admissibility for Torque-Controlled Redundant Robots](https://consensus.app/papers/actuatoraware-inverse-kinematics-with-jointlimit-dastranj-hejrati/9bd7f01daa5c58798faea83094a2103f/?utm_source=chatgpt)

- **书目信息：** Dastranj, Mohammad; Hejrati, Mahdi; Mattila, J.（2026），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2605.31436)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2605.31436`。
- **摘要精读：** 为力矩控制冗余臂建立 actuator-aware QP IK，以 CBF 风格参考速度界限制关节限位逼近，用松弛任务方程及先前命令/力矩能力权重分配冗余；七轴外骨骼实验。
- **与主题的关系：** 从 IK 命令与下游力矩控制相容性角度处理位置限位和关节速度可行性。
- **全文待核：** 特定外骨骼/力矩控制架构；不研究解支连续或奇异过渡。

### 098. [Many-RRT*: Robust Joint-Space Trajectory Planning for Serial Manipulators](https://consensus.app/papers/manyrrt-robust-jointspace-trajectory-planning-for-serial-belmont-christie/5ecbd9939da5551c9a9c25affd9b345c/?utm_source=chatgpt)

- **书目信息：** Belmont, Theodore; Christie, Benjamin; Netchaev, Anton（2026），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2603.04547)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2603.04547`。
- **摘要精读：** Many-RRT* 同时从多个 IK 目标解扩展树，避免选错单一目标分支导致规划失败；跨机构/障碍环境实验，报告成本和成功率提升并称渐近最优。
- **与主题的关系：** 多分支目标集上的关节空间路径规划与选择。
- **全文待核：** 没有固定 Cartesian 工具路径或明确分支连续保证；需查是否靠路径自由度/构型重配置。

### 099. [MimicIK: Real-Time Generative Inverse Kinematics from Teleoperation with FK Consistency](https://consensus.app/papers/mimicik-realtime-generative-inverse-kinematics-from-yang-yan/88e3051936785b439fa2586027c15229/?utm_source=chatgpt)

- **书目信息：** Yang, Jiahao; Yan, Shenhao; Feng, Fan; Yao, Chengsi; Wang, Ge; Mai, Zhixin; Zhao, Yiming; Han, Yatong（2026），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2606.15148)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2606.15148`。
- **摘要精读：** MimicIK 用 teleoperation 示范和 conditional flow matching 学习当前构型到目标位姿的连续 Δq 命令，两步细化并以 FK 一致损失约束；6-DOF 数据集、轨迹指标和 20Hz 实机部署。
- **与主题的关系：** 核心学习式连续 IK，对分支跳变与奇异不稳定有直接动机和实测指标。
- **全文待核：** 未见关节硬位置/速度/加速度约束；受示范数据和 OOD 泛化限制，摘要称 near-singular 稳定但需全文验证。

### 100. [Multi-Solution Inverse Kinematics for Robotic Manipulators via Permutation-Invariant Set Prediction](https://consensus.app/papers/multisolution-inverse-kinematics-for-robotic-nguyen-nguyen/a3b6adaed37259d29dff35b5303e8b96/?utm_source=chatgpt)

- **书目信息：** Nguyen, D.; Nguyen, V.; Truong; Nguyen, V.（2026），IEEE Robotics and Automation Letters；[DOI](https://doi.org/10.1109/lra.2026.3703280)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1109/lra.2026.3703280`。
- **摘要精读：** 将 6-DOF IK 表述为置换不变的多解集合预测，借解析/数值分支种子提供监督，再用连续性感知规则生成命令序列；UR3 实轨迹显示覆盖更多分支且保持跟踪。
- **与主题的关系：** 核心：显式学习无序解集并在轨迹中连续选择分支。
- **全文待核：** 硬关节边界/奇异变化的保证未明；需核查分支可行性筛选和闭环实验配置。

### 101. [Optimized inverse kinematics solutions for a 6-DOF robot](https://consensus.app/papers/optimized-inverse-kinematics-solutions-for-a-6dof-robot-bayoume-abdelgeliel/c82b89748c1a50dbb7a37f7b04073aa4/?utm_source=chatgpt)

- **书目信息：** Bayoume, Mustafa Osman; Abdelgeliel, M.; Saber, E.; El-Gamal, H.（2026），Scientific Reports；[DOI](https://doi.org/10.1038/s41598-026-51032-w)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.1038/s41598-026-51032-w`。
- **摘要精读：** 对 Viper 650s 在统一约束/轨迹/指标下比较六种全局、局部及混合优化 IK，做平面三角与空间螺旋路径重复试验；ACO-B&B-SQP 平均误差最低，SQP 最快。
- **与主题的关系：** 可作为公平统一的优化 IK 路径精度基准。
- **全文待核：** 摘要描述 6-DOF 姿态 IK 优化而非分支跟踪；未见奇异跨越/关节动态界保证。

### 102. [Real-Time Control of Six-DOF Serial Manipulators via Learned Spherical Kinematics](https://consensus.app/papers/realtime-control-of-sixdof-serial-manipulators-via-dharmana-sreedharan/5f902c2284c1512791f8c722bf86a8ac/?utm_source=chatgpt)

- **书目信息：** Dharmana, Meher Madhu; Sreedharan, Pramod（2026），Robotics；[DOI](https://doi.org/10.3390/robotics15010027)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/robotics15010027`。
- **摘要精读：** 球腕 6-DOF 臂用前三关节球坐标低阶多项式、后三腕关节闭式解并微分迭代细化，可枚举最多八个分支；对比 LM/DLS/fmincon。
- **与主题的关系：** 高效完整多解候选生成及奇异附近求解背景。
- **全文待核：** 摘要把自动分支选择列作未来工作，未提供轨迹连续分支算法。

### 103. [Singularity Avoidance in Inverse Kinematics: A Unified Treatment of Classical and Learning-based Methods](https://consensus.app/papers/singularity-avoidance-in-inverse-kinematics-a-unified-rudrasamudram-malaichamee/2402c4c24006507382f283f73d7310d5/?utm_source=chatgpt)

- **书目信息：** Rudrasamudram, Vishnu; Malaichamee, Hariharasudan（2026），ArXiv；[DOI](https://doi.org/10.48550/arxiv.2604.13405)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.48550/arxiv.2604.13405`。
- **摘要精读：** 统一综述经典与学习式奇异鲁棒 IK，提出按几何结构与保障类型分类并在 Panda 上比较 12 个求解器；纯学习策略表现差，经典细化可挽救混合模型。
- **与主题的关系：** 主题分类、评测基准及学习/经典 IK 鲁棒性背景。
- **全文待核：** 位置 IK benchmark，并指出更深奇异区评估为未来工作；不等于连续路径证明。

### 104. [UR3 Collaborative Robot Inverse Kinematics Using Metaheuristic Optimization: A Unified Comparative and Experimental Evaluation](https://consensus.app/papers/ur3-collaborative-robot-inverse-kinematics-using-caballero-mora-sanín-villa/6820a876fa525566aaf7b1efb38d8b0f/?utm_source=chatgpt)

- **书目信息：** Caballero-Mora, J.A.; Sanín-Villa, D.; Girón-Nieto, Huber; Botero-Gómez, Vanessa; López-Romero, Janet; Tejada, Juan（2026），Applied System Innovation；[DOI](https://doi.org/10.3390/asi9070140)。
- **初筛 / 全文状态：** 相邻/背景 / `NOT_STARTED`。
- **摘要来源：** Consensus fetch；Consensus DOI 匹配：`10.3390/asi9070140`。
- **摘要精读：** 在统一可复现协议下比较 UR3 全姿态 IK 的五种元启发式与 LM，含奇异条件惩罚及每姿态 1000 次蒙特卡洛；LM 精度/速度最好，挑选 GWO 做静态和连续多位姿实机验证。
- **与主题的关系：** 统计稳健的数值 IK 对比及多位姿跟踪示例。
- **全文待核：** 方法以静态姿态优化为主；连续序列稳定不等于固定解支/奇异转换保证。

## 全文核读必须继续核对的事项

- 解支标签究竟是解析分支、冗余参数、局部数值状态、图节点还是数据驱动分布；跨时刻关联使用何种状态量。
- 连续性是数值上的相邻帧平滑、数学上的连续，还是可微/有界导数；是否覆盖整条路径而非有限采样点。
- 奇异处是回避、停留、穿越并换支，还是 cuspidal 无奇异切换；存在条件和失败情形是什么。
- 关节限位是代价/投影/经验设置，还是可验证的硬约束；速度、加速度、jerk、力矩/功率与碰撞是否同时满足。
- 实验是仿真、数字孪生、硬件在环还是实机；基线、统计重复、轨迹覆盖、求解时间和控制误差是否支持摘要中的结论。

