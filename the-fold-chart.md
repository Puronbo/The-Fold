# The observer as chart-maker

## What this note is for

The observer is `(d, w)`: a form degree and a window. That pair describes how an observer **reads**.
It does not describe what the observer **writes**. This note adds the missing third term: a chart `C`,
the map the observer builds from the world to a coordinate system, and the loop by which the chart is
revised.

The claim is modest. A calendar is the cleanest example of a chart, and the Fold already has the
arithmetic of calendars — a quotient of periods, a fold for the correction, a closure for the repeat.
Generality, on this reading, is the ability to build and revise the chart, not the size of the window.

## The chart

The observer reads with `(d, w)`. A chart is a map

```
C : W → ℝ^m        with domain D ⊂ W
```

`W` is the world; `D` is the region where the chart is claimed to hold. The chart carries three things
the observer alone does not:

- **coordinates** — what the readings are indexed by;
- **a domain** — where they are valid;
- **a correction rule** — what to do when the coordinates drift.

The window `w` sets the resolution inside `D`. The horizon is `∂D`, the edge where the chart stops.
That is the same horizon as before, now read as the boundary of a chart rather than the boundary of a
cone.

## The calendar is the model chart

A calendar is a quotient of periodicities:

```
day      the rotation              1
month    the lunar or solar cycle
year     the orbit
```

The underlying periods are incommensurable. A calendar is the map that names a date in their product,
and the map cannot be exact — so it carries a **fold**, the leap rule, and a **closure**, the cycle
after which it repeats.

The Gregorian instance is exact arithmetic:

```
400 years = 146,097 days = 7 × 20,871 = 3³ · 7 · 773
```

The divisibility by 7 is the closure. It is why the weekday pattern repeats exactly after 400 years,
and why the calendar is a closed chart rather than a drifting one. The leap rule is the fold:

```
divisible by 4       leap
divisible by 100     not leap
divisible by 400     leap
```

Each line is a correction, and the third overrides the second. The mean year is
`365 + 97/400 = 365.2425` days, close to the tropical `365.2422`. The residual drift is the price of
the quotient; the leap rule is the correction rule that keeps it bounded.

That is the whole structure of a chart: coordinates, a domain, a correction, and a closure. A calendar
is not an external grid laid on time. It is an internal quotient of the periods the observer can
measure.

## The revision loop

A chart that cannot be revised is a fixed coordinate system. Generality is the loop that revises it:

```
world → observation → chart → action → world
              ↑                        ↓
              └───── self-model ←─ horizon ┘
```

The first loop is narrow: read, predict, act. The second loop is the one that matters: the chart
models its own domain and its own correction rule, and changes them when the horizon moves.

In one line:

```
F : (C, D) ↦ (C′, D′)
```

A general observer is a stable fixed point or limit cycle of `F` that preserves the invariants the
action depends on. The "I" is the residue that survives the return — the part of the chart that is
still the same chart after revision.

This is a criterion, not a recipe. It says what generality would have to be; it does not build it.

## The three grades

| grade | chart | failure |
|---|---|---|
| narrow | fixed `C`, fixed `D` | works until the horizon moves |
| general | chooses `C`, tracks `D` | needs a horizon detector |
| meta-general | builds a chart of charts | needs a criterion for when a chart is a chart |

The calendar test is the smallest instance. An observer that can only use the calendar it was given is
narrow. One that can find the periods, choose the epoch, write the leap rule, and state the horizon has
built a calendar. One that can compare two calendars — and say which is better for which purpose — is
doing the meta step.

The first calendar is arithmetic. That is why the Fold can speak about this at all: the closure
`m = π/α`, the sampling bound `N > 2m`, and the crystallographic restriction are already statements
about which periodic charts are possible.

## The horizon detector

A chart without a horizon detector drifts into false confidence. The detector is the chart's own leap
rule: the test that says *the coordinates no longer match the world*.

Three signals, in increasing strength:

- **residual** — the correction term grows instead of staying bounded;
- **disagreement** — two charts of the same domain stop agreeing on the overlap;
- **failure of action** — the prediction is right and the action still fails, so the chart's
  coordinates are the wrong coordinates.

The third is the important one. A chart can be internally consistent and still be the wrong chart.
Consistency is not truth; it is only the absence of an internal contradiction.

## What this is not

The note is a criterion, and the criterion has clear edges:

- **Scale is not generality.** A larger window resolves more inside the same chart; it does not teach
  the observer that the chart is a chart.
- **Data is not a horizon.** More coverage widens `D`; it does not locate `∂D`.
- **An oracle is not general.** An answer without a chart cannot be revised, and cannot say when it is
  wrong.
- **A calendar is not time.** It is a quotient of measured periods; the periods are the world, the
  calendar is the chart.

The false friend is the sentence "more is more general." The exact version is: more can widen the
chart; only revision can change it.

## The zones

| claim | zone |
|---|---|
| the observer is a pair `(d, w)` | exact |
| a chart adds coordinates, a domain, and a correction rule | exact as a definition |
| a calendar is a quotient of periods | exact |
| the Gregorian closure is `146,097 = 7 × 20,871` days | exact |
| the leap rule is a fold with an overriding correction | exact as a reformulation |
| generality is chart revision | exact as a definition; the mechanism is open |
| the horizon is the boundary of the chart's domain | exact as a model |
| scale alone yields generality | false friend |
| data alone yields a horizon | false friend |
| an oracle is general | false friend |
| a calendar is time | false friend |
| a chart is the territory | false friend |
| the "I" is the residue of the revision loop | rhyme |

## Closing

The observer reads with `(d, w)`. The chart is what the observer writes. Generality is the loop that
rewrites it without losing the invariants that make action possible.

A calendar is the smallest complete chart: periods, a quotient, a fold, a closure, a horizon. It is
exact arithmetic, and it is enough to show the shape.

**A narrow observer uses a chart. A general observer makes one. A general observer that knows the
chart is a chart can make another.**
