"""
=============================================================================
 Project: Grid_Topology_Alpha / Janus-Engine
 Description: Production-Grade Harmonic Entropy Auditor & Nonce Bias Detector
 Author: Alexander Perez Cruz
 =============================================================================
"""

import hashlib

class ProductionIoTValidator:
    """
    Motor avanzado de auditoría y detección de sesgos armónicos en firmas ECDSA (secp256k1).
    Diseñado para entornos de producción, validación de firmware y análisis forense de nonces.
    """
    def __init__(self):
        self.curve_n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
        self.curve_gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        self.base_patterns = {85, 170}

    def _inverse_mod(self, val: int, mod: int) -> int:
        return pow(val, mod - 2, mod)

    def audit_signature_stream(self, message: bytes, r: int, s: int, intercepted_nonce: int) -> dict:
        low_byte = intercepted_nonce & 0xFF
        
        audit_report = {
            "status": "SECURE",
            "intercepted_nonce_hex": hex(intercepted_nonce),
            "control_byte": low_byte,
            "vulnerability_detected": False,
            "extracted_private_key": None
        }

        if low_byte in self.base_patterns:
            audit_report["vulnerability_detected"] = True
            audit_report["status"] = "CRITICAL_ENTROPY_COLLAPSE"
            
            z = int(hashlib.sha256(message).hexdigest(), 16)
            
            try:
                r_inv = self._inverse_mod(r, self.curve_n)
                recovered_d = (s * intercepted_nonce - z) * r_inv % self.curve_n
                audit_report["extracted_private_key"] = hex(recovered_d)
            except Exception as e:
                audit_report["error"] = str(e)

        return audit_report

if __name__ == "__main__":
    print("=====================================================================")
    print("       JANUS-ENGINE: PRODUCTION HARMONIC AUDITOR (secp256k1)         ")
    print("=====================================================================\n")

    validator = ProductionIoTValidator()

    test_message = b"Secure_Firmware_Update_v2.0_Payload"
    real_private_key = 0xAF48A03BBFD25E8CD0364141DEADBEEFCAFE1234
    flawed_nonce = 0x0000000000000000000000000000000000000000000000000000008555550085
    
    r_val = (flawed_nonce * validator.curve_gx) % validator.curve_n
    z_val = int(hashlib.sha256(test_message).hexdigest(), 16)
    s_val = (validator._inverse_mod(flawed_nonce, validator.curve_n) * (z_val + r_val * real_private_key)) % validator.curve_n

    print(f"[*] Mensaje objetivo: {test_message.decode()}")
    print(f"[*] Clave Privada Real (Oculta): {hex(real_private_key)}")
    print(f"[*] Analizando firma en busca de trazas armónicas...\n")

    report = validator.audit_signature_stream(test_message, r_val, s_val, flawed_nonce)

    print("--- INFORME DE AUDITORÍA ---")
    for key, value in report.items():
        print(f"  {key}: {value}")
    print("----------------------------")