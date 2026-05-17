# orb_factory.py
# SIRIUS LOCAL AI – ORB FACTORY 4.3.x
# Phase‑4 safe-mode compatible ORB assembly system

from .engine import (
    AnimationEngine,
    OrbObject,
    OrbRingObject,
    OrbGlowObject,
    OrbStateController,
    OrbThinkingEffect,
    OrbWarningFlash,
    OrbSuccessBurst,
    OrbEnergyFlow,
    OrbBreathingEffect,
    OrbIntelligencePulse,
    OrbLinkEffect,
    OrbEnergyField,
    OrbNeuralPathways,
    OrbDecisionMap,
    OrbSynapseSparks,
    OrbMemoryRings,
    OrbLogicFlow,
    OrbConsciousnessField,
    OrbReasoningWaves,
    OrbMetaThoughtLayers,
    OrbSelfReflectionPulse,
    OrbTemporalEchoes,
    OrbPredictiveTrails,
    OrbCognitiveMesh,
    OrbFocusBeam,
    OrbAwarenessBloom,
    OrbQuantumFluctuations,
    OrbSuperposition,
    OrbProbabilityCloud,
    OrbHyperFocus,
    OrbDimensionalShift,
    OrbRealityDistortion,
    OrbEchoNetwork,
    OrbDeepInsightBurst,
    OrbEmergentThoughtLayers,
    OrbCognitiveResonance,
    OrbInsightConvergence,
    OrbAwarenessHalo,
    OrbDeepReflectionField,
    OrbUnifiedCore,
    OrbHarmonicFieldMatrix,
    OrbInsightSingularity,
    OrbCognitiveRipple,
    OrbTotalityLayer
)


def create_sirius_orb():
    """
    Create a fully assembled SIRIUS ORB (Phase‑4).

    Returns:
        (engine, orb) tuple

    Safe‑mode:
        - returns empty engine + core orb only
        - no animation layers are attached

    Degraded‑mode:
        - returns engine with partial layers
        - failures do not break the factory
    """

    engine = AnimationEngine()

    try:
        # Core ORB
        orb = OrbObject()

        # All ORB layers (Phase‑4)
        layers = [
            orb,
            OrbRingObject(),
            OrbGlowObject(),
            OrbStateController(orb),

            # Thinking / warning / success / flow
            OrbThinkingEffect(),
            OrbWarningFlash(),
            OrbSuccessBurst(),
            OrbEnergyFlow(),

            # Breathing / pulse / link / field
            OrbBreathingEffect(orb),
            OrbIntelligencePulse(orb),
            OrbLinkEffect(),
            OrbEnergyField(),

            # Neural / decision / synapse / memory / logic
            OrbNeuralPathways(),
            OrbDecisionMap(),
            OrbSynapseSparks(),
            OrbMemoryRings(),
            OrbLogicFlow(),

            # Consciousness / reasoning / meta-thought / reflection
            OrbConsciousnessField(),
            OrbReasoningWaves(),
            OrbMetaThoughtLayers(),
            OrbSelfReflectionPulse(),

            # Temporal / predictive / mesh / focus / awareness
            OrbTemporalEchoes(),
            OrbPredictiveTrails(),
            OrbCognitiveMesh(),
            OrbFocusBeam(),
            OrbAwarenessBloom(),

            # Quantum / superposition / probability / hyper-focus
            OrbQuantumFluctuations(orb),
            OrbSuperposition(),
            OrbProbabilityCloud(),
            OrbHyperFocus(orb),

            # Dimensional / reality / echo network / deep insight
            OrbDimensionalShift(orb),
            OrbRealityDistortion(),
            OrbEchoNetwork(),
            OrbDeepInsightBurst(),

            # Emergent / resonance / convergence / halo
            OrbEmergentThoughtLayers(),
            OrbCognitiveResonance(orb),
            OrbInsightConvergence(),
            OrbAwarenessHalo(),

            # Final unified layers
            OrbUnifiedCore(orb),
            OrbHarmonicFieldMatrix(),
            OrbInsightSingularity(),
            OrbCognitiveRipple(),
            OrbTotalityLayer(orb),
        ]

        # Register all objects
        for obj in layers:
            try:
                engine.add_object(obj)
            except Exception:
                # Individual layer failure → skip, engine continues
                engine.degraded_mode = True

        return engine, orb

    except Exception:
        # Global failure → degraded mode with minimal ORB
        engine.degraded_mode = True
        orb = OrbObject()
        engine.add_object(orb)
        return engine, orb
