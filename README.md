# Boundary-Criticality Framework

## A Testable Cross-Domain Risk Model for Boundary-Governed Transitions

> **Status:** Hypothesis / modeling framework  
> **Purpose:** Mathematical, scientific, engineering, and systems review  
> **Core claim:** Transition risk can often be modeled as the interaction between boundary, deviation, pressure, capacity, noise, adaptation, and transition channel.

---

## Author Note

This document proposes a hypothesis and modeling framework for systems that appear to undergo qualitative transitions when pressure builds against a boundary.

It is **not** presented as a proven universal law.

It is presented as a **testable abstraction** for mathematical, scientific, engineering, and systems review.

The goal is to make the idea precise enough that it can be challenged, formalized, improved, or rejected.

---

## Abstract

Many systems appear to change state when deviation from an admissible or stable region is no longer contained by a boundary.

Examples may include avalanches in granular systems, decisions in neural evidence accumulation, failures in software systems, overload in institutions, and transitions in physical or social systems.

This document proposes the **Boundary-Criticality Hypothesis**:

> A boundary-governed system becomes transition-prone when unresolved deviation from its admissible region creates pressure that exceeds, weakens, escapes, or outpaces the effective containment capacity of a boundary, provided that a transition channel exists.

The hypothesis is not that pressure always causes transition.

Instead, it proposes that transition risk depends on the interaction between:

- boundary
- deviation
- pressure
- capacity
- noise
- adaptation
- transition channel

The central object is therefore not always deterministic transition.

In many systems, especially noisy systems, the correct object is:

$$
P(\tau_B \leq T)
$$

not:

$$
\text{transition} \in \{\text{yes}, \text{no}\}
$$

---

## 1. Core Intuition

A system may have a region in which its behavior is considered stable, valid, admissible, or contained.

A boundary defines that region.

When the system moves away from that region, deviation appears.

If deviation persists, spikes, accelerates, fluctuates, or weakens the boundary, it may create pressure.

If that pressure overcomes effective containment, and if the system has an available transition path, the system may reorganize, fracture, reject, collapse, commit, escape, or transform.

Compact intuition:

$$
\text{boundary} + \text{deviation} + \text{pressure} + \text{capacity} + \text{channel}
\longrightarrow
\text{transition risk}
$$

A simpler public shorthand is:

> Contained difference against boundary capacity creates transition risk.

But the stronger version is:

> Pressure does not guarantee transition.  
> Pressure increases transition risk through a boundary and a channel.

---

## 2. Hypothesis Statement

A boundary-governed system becomes transition-prone when unresolved deviation from its admissible region creates pressure that exceeds, weakens, escapes, or outpaces the effective containment capacity of a boundary, provided that a transition channel exists.

In deterministic low-noise systems, this may appear as threshold crossing.

In stochastic or noisy systems, the appropriate object is transition probability:

$$
P(\tau_B \leq T)
$$

where:

- **$\tau_B$**: first transition time through boundary $B$
- **$T$**: time horizon

---

## 3. Boundary-Criticality Risk Equation

The proposed general risk form is:

$$ P(\tau_B \leq T) = q_{\Gamma_B} \max \left( p_{FP}, \max_{k \in K}(p_k) \right) $$

*(Note: This aggregation is a heuristic bound, not a derived first-principles risk measure. The `max` function treats different pressure modes as competing, mutually exclusive risks to avoid artificially inflating probability when modes are highly correlated. A true first-principles derivation would require a formal coupled competing-risks model or copula aggregation.)*

where each pressure-mode probability is modeled using a bounded continuous function to ensure $p_k = 0$ when $\phi_k = 0$:

$$
p_k = 1 - \exp\left( - \left( \frac{\phi_k}{C_k} \right)^{\lambda_k} \right)
$$

*(Caveat: This exponential/Weibull form is mathematically plausible but arbitrary. It biases the model toward smooth thresholds. In many physical or complex systems, near-critical behavior follows power laws rather than exponentials. The mapping function should be adjusted based on domain-specific criticality mechanics.)*

---

## 4. Meaning of the Terms

- **$\tau_B$**: First transition time through boundary $B$.
- **$T$**: Time horizon.
- **$q_{\Gamma_B}$**: Probability or availability of a transition channel.
- **$p_{FP}$**: First-passage probability for noisy boundary escape.
- **$p_k$**: Probability contribution from pressure mode $k$.
- **$\phi_k$**: Measured pressure feature.
- **$C_k$**: Capacity associated with pressure feature $k$.
- **$\lambda_k$**: Sharpness of the transition around the threshold.
- **$K$**: Set of selected pressure modes.

If no transition channel exists, pressure may produce degradation, containment, fatigue, normalization, local damage, or rejection without system-level transition.

---

## 5. Pressure Modes

The framework does not assume that only one kind of pressure matters.

Different systems may transition through different pressure signatures.

A practical pressure set may include the following modes.

---

### 5.1 Accumulated Deviation

$$
\phi_A = \int_0^T \max(0, D_B(t)) e^{-\gamma(T-t)}\,dt
$$

*(where $\gamma$ is the system's natural recovery or dissipation rate, preventing infinite buildup from negligible deviations over long periods)*

This applies when transition depends on buildup over time.

Examples:

- fatigue
- stress accumulation
- evidence accumulation
- long-term institutional pressure
- resource exhaustion

---

### 5.2 Peak Deviation

$$
\phi_M = \max_{0 \leq t \leq T} D_B(t)
$$

This applies when one large shock can trigger transition.

Examples:

- impact failure
- traffic spike
- sudden overload
- single invalid request
- acute institutional shock

---

### 5.3 Rate of Change

$$
\phi_R = \max_{0 \leq t \leq T} \left|\Delta D_B(t)\right|
$$

This applies when rapid change matters more than total accumulated pressure.

Examples:

- market panic
- rapid destabilization
- resonance
- sudden neural switching
- fast cascading failure

---

### 5.4 Volatility

$$
\phi_V = \mathrm{Var}(D_B(t))
$$

This applies when instability, fluctuation, or variance predicts transition risk.

Examples:

- noisy systems
- critical slowing down
- unstable decision systems
- financial volatility
- feedback-sensitive systems

---

### 5.5 Fatigue or Weakening

$$
\phi_F = F_B(T)
$$

This applies when pressure changes the boundary itself.

Examples:

- material fatigue
- institutional legitimacy loss
- policy erosion
- trust decay
- infrastructure weakening

---

### 5.6 Topological Weak-Point Stress

$$
\phi_G = G_B(S_{0:T})
$$

This applies when failure depends on structure rather than total pressure.

Examples:

- network bottlenecks
- bridge cracks
- dependency chains
- single points of failure
- institutional choke points
- software architecture weak spots

---

## 6. Stochastic Boundary Escape

In noisy systems, transition should not be modeled as guaranteed threshold crossing.

Random fluctuation may cause transition before accumulated pressure becomes large.

Accumulated deviation may also occur without true boundary escape.

Therefore, stochastic boundary-criticality should use first-passage probability.

For a noisy process with drift:

$$
S_{t+1} = S_t + \mu + \sigma \xi_t
$$

where:

- **$S_t$**: system state
- **$\mu$**: drift toward or away from the boundary
- **$\sigma$**: noise strength
- **$\xi_t$**: random fluctuation
- **$C$**: boundary capacity

Transition occurs when:

$$
S_t \geq C
$$

The first transition time is:

$$
\tau_C = \inf \{t : S_t \geq C\}
$$

The relevant object is:

$$
P(\tau_C \leq T)
$$

For a Brownian or noisy process with drift, the continuous-time first-passage approximation is:

$$ P(\tau_C \leq T)
\Phi\left(\frac{\mu T - C_{\mathrm{eff}}}{\sigma\sqrt{T}}\right) + \exp\left(\frac{2\mu C_{\mathrm{eff}}}{\sigma^2}\right) \Phi\left(\frac{-\mu T - C_{\mathrm{eff}}}{\sigma\sqrt{T}}\right) $$

For zero drift:

$$ P(\tau_C \leq T)
2\left[1 - \Phi\left(\frac{C_{\mathrm{eff}}}{\sigma\sqrt{T}}\right)\right] $$

For discrete-time simulations of simple random walks, an effective-boundary correction overshoot is often required:

$$
C_{\mathrm{eff}} \approx C + 0.5\sigma
$$

**Important Caveat:** This correction is highly specific to discrete-time Gaussian steps. It fails for continuous-time processes, drift-heavy regimes, correlated noise (colored noise), or fat-tailed jump processes (Lévy flights). It is included here strictly as a practical discrete-simulation placeholder, not a universal boundary shift.

---

## 7. Transition Channels

Pressure alone is not enough.

A system also needs an available transition channel.

The transition channel is:

$$
\Gamma_B
$$

It represents the set of available state transformations that can convert boundary pressure into qualitative change.

A transition channel may include:

- escape
- fracture
- collapse
- rejection
- approval
- commitment
- phase change
- reorganization
- adaptation
- quarantine
- rollback

If:

$$
\Gamma_B = \varnothing
$$

then pressure may not produce transition.

It may produce:

- degradation
- fatigue
- normalization
- containment
- local damage
- hidden instability

**Critical requirement:** The existence of a transition channel $\Gamma_B$ must be observable ex-ante, independently of whether a transition occurs. Otherwise, the model becomes an unfalsifiable tautology where all failed transitions are simply retroactively blamed on "no channel."

This prevents the hypothesis from falsely claiming that high pressure always causes transition.

The practical rule is:

$$
\text{pressure} + \text{no channel}
\longrightarrow
\text{degradation or containment}
$$

$$
\text{pressure} + \text{channel}
\longrightarrow
\text{transition risk}
$$

---

## 8. Capacity

Boundary capacity is not a universal constant.

It must be defined by domain.

$$
C_B(t)
$$

is the effective containment capacity of boundary $B$ at time $t$.

It may strengthen, weaken, adapt, or collapse over time. In complex adaptive systems, capacity often co-evolves with historical pressure (e.g., biological hypertrophy, material self-healing, or institutional learning). 

Without formalizing this dynamical feedback, the model is incomplete and risks post-hoc rationalization. If capacity adapts faster than pressure accumulates ($\frac{dC_k}{dt} > \frac{d\phi_k}{dt}$), the system will *not* transition despite high absolute pressure. A complete dynamical systems formulation must couple pressure to capacity:

$$
\frac{dC_B(t)}{dt} = f(\phi_{0:t-1}, C_{0:t-1}) - \text{decay}
$$

---

### Examples of Capacity by Domain

- **Physical systems**: yield strength, fracture toughness, energy barrier, load limit, thermal threshold
- **Stochastic systems**: distance to absorbing boundary, escape barrier, noise-adjusted threshold
- **Control systems**: safety margin, viability margin, stability reserve, constraint boundary
- **Neural and decision systems**: decision threshold, activation threshold, attractor basin boundary, commitment boundary
- **Software governance systems**: authorization boundary, policy threshold, constraint set, approval condition, execution gate
- **Social and institutional systems**: resilience capacity, legitimacy reserve, enforcement capacity, adaptive reform capacity, trust reserve

The important requirement is:

> $C_B(t)$ should be defined before evaluating transition.

If capacity is only defined after the transition is observed, the hypothesis becomes circular.

---

## 9. Deterministic Limiting Case

The deterministic threshold version is a special case.

If:

- noise is negligible
- capacity is fixed
- one pressure mode dominates
- a transition channel is available
- the threshold is sharp

then the framework can reduce to:

$$
\phi_k \geq C_k \longrightarrow \text{transition}
$$

or, for accumulated deviation:

$$
\int_0^T \max(0, D_B(t))\,dt \geq C_A
\longrightarrow
\text{transition}
$$

But this should be treated as a limiting case, not the universal rule.

The general version is probabilistic:

$$
P(\tau_B \leq T)
$$

not always deterministic:

$$
\text{transition} / \text{no transition}
$$

---

## 10. Stress-Test Summary

The proposed risk equation was tested against five synthetic boundary systems.

The purpose was not to prove the hypothesis universally.

The purpose was to test whether the formula survives obvious failure cases better than a simple accumulation-only rule.

Tested systems:

1. accumulation-driven transition
2. peak-shock transition
3. rate-shock transition
4. stochastic/noisy boundary escape
5. channel-limited transition

Each system was tested with **100,000 simulated runs**.

Total simulated runs:

$$
500{,}000
$$

The accumulation-only rule failed when transition was caused by peak shock, rate shock, stochastic escape, or channel limitation.

The boundary-criticality risk equation performed better because it allowed different pressure modes, noise, and transition-channel availability.

### Summary

- Accumulation-only models overpredict transition when pressure does not have a channel.
- Accumulation-only models underdescribe transitions caused by sudden shock or rapid change.
- Noisy systems require first-passage probability, not deterministic implication.
- Transition risk is better modeled as pressure mode + capacity + noise + channel.

A representative stochastic test used:

$$
T = 100, \qquad C = 12, \qquad \mu = 0, \qquad \sigma = 1
$$

The corrected first-passage prediction was approximately:

$$
21.13\%
$$

The simulated transition rate was approximately:

$$
21.0\% \text{ to } 21.2\%
$$

This supports the use of the stochastic version as a risk model in noisy boundary systems.

It does not prove universal validity.

---

## 11. Relationship to Existing Theory

This framework may overlap with several existing mathematical and scientific theories.

That overlap is expected.

In some domains, boundary-criticality may reduce to known models.

- **First-passage theory**: When the system is a stochastic process crossing a boundary, the framework becomes first-passage analysis.
- **Catastrophe and bifurcation theory**: When the system shifts between attractor regimes, the framework overlaps with catastrophe theory and bifurcation theory.
- **Self-organized criticality**: When the system accumulates instability and releases through avalanches, the framework overlaps with self-organized criticality.
- **Control and viability theory**: When the system is governed by admissible regions and safety constraints, the framework overlaps with control theory, viability theory, and safety-boundary analysis.
- **Barrier-crossing models**: When the system escapes over an energy or potential barrier, the framework overlaps with barrier-crossing and escape-rate models.
- **Drift-diffusion and evidence accumulation**: When the system accumulates evidence toward a decision threshold, the framework overlaps with drift-diffusion models and evidence accumulation.

Therefore, the novelty claim should be modest.

The framework may not replace these theories.

Its possible value is as a cross-domain language for identifying a shared structure:

$$
\text{boundary}
\rightarrow
\text{deviation}
\rightarrow
\text{pressure}
\rightarrow
\text{capacity}
\rightarrow
\text{noise}
\rightarrow
\text{channel}
\rightarrow
\text{transition}
$$

---

## 12. Predictive Status

At its current stage, the framework is strongest as a unifying and testable modeling structure.

It becomes predictive only when its terms are fixed before observation.

A valid application must define the following before evaluating whether a transition occurs:

- **$B$**: boundary
- **$\Omega_B$**: admissible or stable region
- **$D_B$**: deviation from the admissible region
- **$\phi_k$**: selected pressure modes
- **$C_k$**: capacity for each pressure mode
- **$\lambda_k$**: threshold sharpness for each mode
- **$q_{\Gamma_B}$**: transition-channel availability
- **$p_{FP}$**: first-passage probability, when noise is relevant
- **$T$**: time horizon
- **transition criterion**: definition of what counts as a transition

The framework makes several testable predictions.

---

### Prediction 1

Accumulation-only models should fail in shock-driven systems.

Peak deviation should outperform accumulated deviation when transitions are caused by sudden overload.

---

### Prediction 2

Accumulation-only models should fail in rate-driven systems.

Rate of change should outperform accumulated deviation when transitions are caused by rapid destabilization.

---

### Prediction 3

Noisy systems should be modeled by first-passage probability, not deterministic threshold implication.

---

### Prediction 4

Systems with high pressure but no transition channel should show degradation, normalization, containment, or fatigue rather than clean transition.

---

### Prediction 5

Capacity adaptation changes transition timing.

If capacity strengthens, transition risk may fall.

If capacity weakens, transition risk may rise.

---

## 13. Application Procedure

To apply the Boundary-Criticality Hypothesis in a real domain:

### Step 1 — Define the boundary

What separates admissible from non-admissible behavior?

### Step 2 — Define the stable or admissible region

$$
\Omega_B
$$

### Step 3 — Define deviation

$$
D_B(S(t), \Omega_B)
$$

This must be domain-specific.

### Step 4 — Select pressure features before testing

Possible features:

- accumulation
- peak
- rate
- volatility
- fatigue
- topology

### Step 5 — Define capacity for each selected pressure mode

$$
C_k
$$

### Step 6 — Define whether a transition channel exists

$$
\Gamma_B
$$

### Step 7 — If the system is noisy, estimate first-passage probability

$$
p_{FP}
$$

### Step 8 — Compute transition risk

$$
P(\tau_B \leq T)
$$

### Step 9 — Compare predictions against evidence

Compare predictions against held-out simulations, historical data, or experiments.

### Step 10 — Downgrade if needed

If the model does not outperform simpler existing models, treat the framework as descriptive rather than predictive in that domain.

---

## 14. Example Domain Interpretations

### Sandpile or Avalanche Systems

- **Boundary**: slope stability
- **Deviation**: local instability
- **Pressure**: accumulated grains, local overload, topology of unstable regions
- **Transition**: avalanche
- **Related theory**: self-organized criticality

---

### Neural Decision Systems

- **Boundary**: decision threshold
- **Deviation**: evidence displacement toward a choice
- **Pressure**: evidence accumulation, drift, noise, urgency
- **Transition**: commitment to decision
- **Related theory**: drift-diffusion models

---

### Software Governance Systems

- **Boundary**: authorization and policy constraints
- **Deviation**: request outside permitted authority
- **Pressure**: constraint violation, repeated attempts, suspicious arguments, escalation demand
- **Transition**: approve, reject, quarantine, execute, rollback
- **Related theory**: control systems, safety constraints, formal policy enforcement

---

### Social and Institutional Systems

- **Boundary**: institutional legitimacy and operational stability
- **Deviation**: unresolved tension, loss of trust, unmet demands
- **Pressure**: accumulated tension, rapid shocks, network contagion, legitimacy decay
- **Transition**: reform, collapse, adaptation, revolt, fragmentation
- **Related theory**: complex systems, critical transitions, network contagion

---

## 15. Falsifiability

The hypothesis can fail.

It should be considered weakened or false in a domain if:

- its terms cannot be defined before observation
- it does not outperform simpler models
- transition occurs independently of boundary, deviation, capacity, noise, or channel
- pressure features do not correlate with transition risk
- capacity estimates have no predictive value
- transition channels cannot be meaningfully identified

The framework should not be protected by redefining terms after the outcome is known.

That would make it unfalsifiable. The most dangerous practical tautology is the transition channel $\Gamma_B$. In social or software systems, an "available channel" often only becomes visible *after* a transition has exploited it. A strong, valid test requires predicting and independently observing $\Gamma_B$ **before** the transition occurs.

---

## 16. Current Assessment

Boundary-criticality is **not** a universal law.

It is a candidate cross-domain risk framework for boundary-governed transitions.

Its strongest claim is:

> Many qualitative transitions can be modeled as risk emerging from the interaction between deviation pressure, effective boundary capacity, noise, adaptation, and available transition channels.

Its weakest point is:

> It becomes vague if the boundary, deviation, capacity, pressure features, and transition channel are not defined before testing.

Its best use is:

> A formal checklist for turning vague transition language into testable models.

---

## Final Compact Statement

> A boundary does not break because difference exists.
>
> A boundary becomes transition-prone when difference creates pressure that exceeds, escapes, weakens, or outruns containment — and when a channel exists for the system to change state.
